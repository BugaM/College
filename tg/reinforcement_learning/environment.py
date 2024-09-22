import gym
import numpy as np
import time
from gym import spaces

from constants.robot_constants import TOLERANCE, MAX_WHEEL_SPEED, MAX_VELOCITY, MAX_ANGULAR
from constants.field_constants import WIDTH, HEIGHT
from constants.simulation_constants import SIMULATION_STEPS_PER_EVALUATION
from decision_making.decision import ReinforcementLearningDecision
from simulation import Simulation
from utils import constrain_angle

MIN_WIDTH = WIDTH
MIN_HEIGHT = HEIGHT

class CustomEnv(gym.Env):
    def __init__(self, render: bool):
        super(CustomEnv, self).__init__()
        self.decision = ReinforcementLearningDecision()
        self.simulation = Simulation(self.decision, render=render)
        self.reset()
        obs_low, obs_high = self.get_observation_boundaries()
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=self.get_action_space_size(), dtype=np.float32)
    
    @classmethod
    def get_observation_boundaries(cls):
        obs_low = np.array([
            -2*WIDTH,     # Min relative x-position
            -2*HEIGHT,    # Min relative y-position
            -np.pi,     # Min relative psi
            -MAX_WHEEL_SPEED,  # Min wheel speed
            -MAX_WHEEL_SPEED,
            -MAX_WHEEL_SPEED,
            -MAX_WHEEL_SPEED,
            -MAX_VELOCITY,     # Min velocity 
            -MAX_VELOCITY,
            -MAX_ANGULAR       #Min Angular
        ], dtype=np.float32).reshape(10,1)

        obs_high = np.array([
            2*WIDTH,      # Max relative x-position
            2*HEIGHT,     # Max relative y-position
            np.pi,      # Max relative psi
            MAX_WHEEL_SPEED,   # Max wheel speed
            MAX_WHEEL_SPEED,
            MAX_WHEEL_SPEED,
            MAX_WHEEL_SPEED,
            MAX_VELOCITY,   # Max velocity
            MAX_VELOCITY,
            MAX_ANGULAR    # Max angular
        ], dtype=np.float32).reshape(10,1)
        return obs_low, obs_high

    def reset(self):
        self.simulation.reset()

        width = np.random.uniform(0,WIDTH)
        height = np.random.uniform(0,HEIGHT)
        self.target_position = np.array([[width, height]]).T
        self.target_psi = np.random.uniform(-np.pi, np.pi)
        self.start_time = time.time()
        obs = self.get_observation()
        return obs

    def step(self, action):
        self.previous_ws = self.simulation.get_player_ws()
        self.decision.set_ws(action)
        self.simulation.run(SIMULATION_STEPS_PER_EVALUATION * 2,True, False, target=np.concatenate((self.target_position, np.reshape(self.target_psi,(1,1)))))
        obs = self.get_observation()

        reward = self.compute_reward()
        done = self.check_done()
        return obs, reward, done, {}

    def get_observation(self):
        player_pos = self.simulation.get_player_pos()
        player_psi = self.simulation.get_player_psi()
        player_ws = self.simulation.get_player_ws()
        player_v = self.simulation.get_player_vs()

        relative_pos = self.target_position - player_pos
        relative_psi = np.reshape(constrain_angle(self.target_psi - player_psi), (1,1))

        return np.concatenate((relative_pos, relative_psi,player_ws, player_v))
    
    def get_observation_space_size(self):
        return self.get_observation().shape
    
    def get_action_space_size(self):
        return self.simulation.get_player_ws().shape

    def compute_reward(self):
        player_psi = self.simulation.get_player_psi()
        player_position = self.simulation.get_player_pos()
        player_ws = self.simulation.get_player_ws()

        angle_diff2 = constrain_angle(player_psi - self.target_psi)**2
        max_angle_diff2 = np.pi ** 2
        angle_reward = -angle_diff2/max_angle_diff2

        dist = np.linalg.norm(player_position - self.target_position)
        max_dist = np.linalg.norm((WIDTH, HEIGHT))
        dist_reward = -dist/max_dist


        ws_diff_norm = np.linalg.norm(player_ws - self.previous_ws)
        max_ws_diff_norm = 4 * MAX_WHEEL_SPEED
        ws_reward = -ws_diff_norm/max_ws_diff_norm

        reward = dist_reward + 0.5 * angle_reward + 0.01 * ws_reward
        return reward

    def check_done(self):
        # Define when the episode is done
        player_position = self.simulation.get_player_pos()
        return np.linalg.norm(player_position - self.target_position) < TOLERANCE

    def render(self, mode='human'):
        self.simulation.draw(np.concatenate((self.target_position, np.reshape(self.target_psi,(1,1)))))

    def close(self):
        self.simulation.close()
