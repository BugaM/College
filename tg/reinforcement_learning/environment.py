import gym
import numpy as np
import time
from gym import spaces

from constants.robot_constants import TOLERANCE
from constants.field_constants import WIDTH, HEIGHT
from decision_making.decision import ReinforcementLearningDecision
from simulation import Simulation

class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        self.decision = ReinforcementLearningDecision()
        self.simulation = Simulation(self.decision, True)  # Initialize your simulation with no decision
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(self.get_observation_space_size(),), dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.get_action_space_size(),), dtype=np.float32)
        self.target_position = np.array([[100, 100]]).T  # Example target position
        self.target_psi = 0

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
        self.simulation.run(1,True, False)
        obs = self.get_observation()

        # TODO
        reward = self.compute_reward()
        done = self.check_done()
        return obs, reward, done, {}

    def get_observation(self):
        player_pos = self.simulation.get_player_pos()
        player_psi = self.simulation.get_player_psi()
        player_ws = self.simulation.get_player_ws()
        player_v = self.simulation.get_player_vs()

        relative_pos = self.target_position - player_pos
        relative_psi = np.reshape(self.target_psi - player_psi, (1,1))

        return np.concatenate((relative_pos, relative_psi,player_ws, player_v))
    
    def get_observation_space_size(self):
        return 10
    
    def get_action_space_size(self):
        return 4

    def compute_reward(self):
        reward = 0
        player_psi = self.simulation.get_player_psi()
        player_ws = self.simulation.get_player_ws()

        angle_diff2 = (player_psi - self.target_psi)**2
        reward -= angle_diff2

        time_taken = time.time() - self.start_time
        reward -= 0.1 * time_taken

        ws_diff_norm = np.linalg.norm(player_ws - self.previous_ws)
        reward -= 0.1 * ws_diff_norm

        # Add torr?

        return reward

    def check_done(self):
        # Define when the episode is done
        player_position = self.simulation.get_player_pos()
        return np.linalg.norm(player_position - self.target_position) < TOLERANCE

    def render(self, mode='human'):
        self.simulation.draw()

    def close(self):
        self.simulation.close()
