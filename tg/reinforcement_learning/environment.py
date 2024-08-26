import gym
from gym import spaces
from constants.robot_constants import TOLERANCE
from decision_making.decision import ReinforcementLearningDecision
import numpy as np
from simulation import Simulation

class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        self.decision = ReinforcementLearningDecision()
        self.simulation = Simulation(self.decision)  # Initialize your simulation with no decision
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(self.simulation.get_observation_space_size(),), dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.simulation.get_action_space_size(),), dtype=np.float32)
        self.target_position = np.array([[100, 100]]).T  # Example target position
        self.target_psi = 0

    def reset(self):
        self.simulation.reset()
        obs = self.simulation.get_observation()
        return obs

    def step(self, action):

        self.decision.set_ws(action)
        self.simulation.run(1,False, False)
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

    def compute_reward(self):
        # Define the reward function based on your criteria
        robot_position = self.simulation.get_robot_position()
        distance_to_target = np.linalg.norm(robot_position - self.target_position)
        reward = -distance_to_target  # Negative reward proportional to distance
        return reward

    def check_done(self):
        # Define when the episode is done
        robot_position = self.simulation.get_robot_position()
        return np.linalg.norm(robot_position - self.target_position) < TOLERANCE

    def render(self, mode='human'):
        self.simulation.render()

    def close(self):
        self.simulation.close()
