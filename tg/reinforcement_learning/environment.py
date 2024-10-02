import gym
import numpy as np
import time
from gym import spaces

from constants.robot_constants import POSITION_TOLERANCE, ANGLE_TOLERANCE, VELOCITY_TOLERANCE, MAX_WHEEL_SPEED, MAX_VELOCITY, MAX_ANGULAR, MAX_ACC
from constants.field_constants import WIDTH, HEIGHT
from constants.simulation_constants import RL_STEPS
from decision_making.decision import ReinforcementLearningDecision
from simulation import Simulation
from utils import constrain_angle

MIN_WIDTH = WIDTH
MIN_HEIGHT = HEIGHT

class CustomEnv(gym.Env):
    def __init__(self, render: bool = False, seed = 42):
        super(CustomEnv, self).__init__()
        np.random.seed(seed)
        self.decision = ReinforcementLearningDecision()
        self.simulation = Simulation(self.decision, render=render)
        self.hold_history = render
        self.reset()
        obs_low, obs_high = self.get_observation_boundaries()
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=self.get_action_space_size(), dtype=np.float32)
    
    @classmethod
    def get_observation_boundaries(cls):
        obs_low = np.array([
            -WIDTH,     # Min relative x-position
            -HEIGHT,    # Min relative y-position
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
            WIDTH,      # Max relative x-position
            HEIGHT,     # Max relative y-position
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
        self.simulation.reset(random=True)

        width = np.random.uniform(WIDTH/8,7*WIDTH/8)
        height = np.random.uniform(HEIGHT/8,7*HEIGHT/8)
        self.target_position = np.array([[width, height]]).T
        self.target_psi = np.random.uniform(-np.pi, np.pi)
        self.start_time = time.time()
        obs = self.get_observation()
        return obs

    def step(self, action):
        self.previous_ws = self.simulation.get_player_ws()
        self.decision.set_ws(action)
        self.simulation.run(RL_STEPS,self.hold_history, False, target=np.concatenate((self.target_position, np.reshape(self.target_psi,(1,1)))))
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
        player_v = np.linalg.norm(self.simulation.get_player_vs())

        angle_diff = abs(constrain_angle(player_psi - self.target_psi))
        max_angle_diff = np.pi
        angle_reward = -angle_diff/max_angle_diff

        dist = np.linalg.norm(player_position - self.target_position)
        max_dist = np.linalg.norm((WIDTH, HEIGHT))
        dist_reward = -dist/max_dist

        ws_diff_norm = np.linalg.norm(player_ws - self.previous_ws)
        max_ws_diff_norm = 4 * MAX_WHEEL_SPEED
        ws_reward = -ws_diff_norm/max_ws_diff_norm

        tor_reward = 0
        if dist < 5*POSITION_TOLERANCE:
            max_torr_speed = np.sqrt(2*MAX_ACC*dist)
            if player_v > max_torr_speed:
                tor_reward = -(player_v - max_torr_speed)/player_v
    
        reward = dist_reward + 0.1 * angle_reward + 0.002 * ws_reward + 0.005 * tor_reward

        if self.check_done():
            # Large bonus for reaching the desired state
            reward += 10

        return reward

    def check_done(self):
        # Define when the episode is done
        player_position = self.simulation.get_player_pos()
        player_angle = self.simulation.get_player_psi()
        return (np.linalg.norm(player_position - self.target_position) < POSITION_TOLERANCE and
                abs(constrain_angle(player_angle - self.target_psi)) < ANGLE_TOLERANCE and
                np.linalg.norm(self.simulation.get_player_vs()) < VELOCITY_TOLERANCE)

    def render(self, mode='human'):
        self.simulation.draw(np.concatenate((self.target_position, np.reshape(self.target_psi,(1,1)))))

    def close(self):
        self.simulation.close()
