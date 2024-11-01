import gym
import numpy as np
from gym import spaces

from constants.robot_constants import POSITION_TOLERANCE, ANGLE_TOLERANCE, VELOCITY_TOLERANCE, MAX_WHEEL_SPEED, MAX_VELOCITY, MAX_ANGULAR, MAX_ACC
from constants.field_constants import *
from constants.noise import STTDEV_ROBOT_P, STDDEV_TARGET_P, STDEV_TARGET_PSI, STDEV_ROBOT_PSI
from constants.simulation_constants import RL_STEPS
from decision_making.decision import ReinforcementLearningDecision
from simulation import Simulation
from utils import constrain_angle


class CustomEnv(gym.Env):
    def __init__(self, render: bool = False, seed = 42, n_angles = 12, num_opps = 9,  add_noise = True, draw_lidar = False):
        super(CustomEnv, self).__init__()
        np.random.seed(seed)
        self.decision = ReinforcementLearningDecision()
        self.add_noise = add_noise
        self.n_angles = n_angles
        self.simulation = Simulation(self.decision, render=render, num_opps=num_opps, lidar_angles=n_angles, draw_lidar=draw_lidar)
        self.hold_history = render
        self.reset()
        obs_low, obs_high = self.get_observation_boundaries()
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.float32)
        self.action_space = spaces.Box(low=-1, high=1, shape=self.get_action_space_size(), dtype=np.float32)
    
    def get_observation_boundaries(self):
        MAX_DIST = np.sqrt(WIDTH**2 + HEIGHT**2)
        obs_low = np.array([
            -MAX_DIST,     # Min relative x-position
            -MAX_DIST,    # Min relative y-position
            -np.pi,     # Min relative psi
            -MAX_WHEEL_SPEED,  # Min wheel speed
            -MAX_WHEEL_SPEED,
            -MAX_WHEEL_SPEED,
            -MAX_WHEEL_SPEED,
            -MAX_VELOCITY,     # Min velocity 
            -MAX_VELOCITY,
            -MAX_ANGULAR       #Min Angular
        ] + 
        [0] * self.n_angles, # Lidar reads
        dtype=np.float32).reshape(10 + self.n_angles,1)

        obs_high = np.array([
            MAX_DIST,      # Max relative x-position
            MAX_DIST,     # Max relative y-position
            np.pi,      # Max relative psi
            MAX_WHEEL_SPEED,   # Max wheel speed
            MAX_WHEEL_SPEED,
            MAX_WHEEL_SPEED,
            MAX_WHEEL_SPEED,
            MAX_VELOCITY,   # Max velocity
            MAX_VELOCITY,
            MAX_ANGULAR    # Max angular
        ] + 
        [WIDTH] * self.n_angles, # Lidar reads
        dtype=np.float32).reshape(10 + self.n_angles,1)
        return obs_low, obs_high

    def reset(self):
        width = np.random.uniform(ROBOT_MIN_WIDTH_FIELD,ROBOT_MAX_WIDTH_FIELD)
        height = np.random.uniform(ROBOT_MIN_HEIGHT_FIELD, ROBOT_MAX_HEIGHT_FIELD)
        self.target_position = np.array([[width, height]]).T
        self.target_psi = np.random.uniform(-np.pi, np.pi)

        self.simulation.reset(random=True, target=self.target_position)
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
        # Make copies of the values to avoid modifying the original class members
        player_pos = self.simulation.get_player_pos().copy()
        player_psi = self.simulation.get_player_psi()
        player_ws = self.simulation.get_player_ws()
        player_v = self.simulation.get_player_vs()
        lidar_read = self.simulation.get_player_lidar_read().copy()
        target_pos = self.target_position.copy()
        target_psi = self.target_psi

        # Add noise if necessary
        if self.add_noise:
            player_pos_noise = np.random.normal(0, STTDEV_ROBOT_P, 2).reshape(2, 1)
            target_pos_noise = np.random.normal(0, STDDEV_TARGET_P, 2).reshape(2, 1)
            player_psi_noise = np.random.normal(0, STDEV_ROBOT_PSI)
            target_psi_noise = np.random.normal(0, STDEV_TARGET_PSI)
            lidar_read_noise = np.random.normal(0, 2 * STTDEV_ROBOT_P, lidar_read.shape[0]).reshape(lidar_read.shape)

            player_pos += player_pos_noise
            target_pos += target_pos_noise
            player_psi += player_psi_noise
            target_psi += target_psi_noise
            lidar_read += lidar_read_noise

        # Calculate relative position and angle in the agent's frame
        relative_pos = target_pos - player_pos
        cos_psi, sin_psi = np.cos(-player_psi), np.sin(-player_psi)
        relative_pos_agent_frame = np.array([
            cos_psi * relative_pos[0] - sin_psi * relative_pos[1],
            sin_psi * relative_pos[0] + cos_psi * relative_pos[1]
        ])
        relative_psi = np.reshape(constrain_angle(target_psi - player_psi), (1, 1))

        # Return the concatenated observation
        return np.concatenate((relative_pos_agent_frame, relative_psi, player_ws, player_v, lidar_read))

    
    def get_observation_space_size(self):
        return self.get_observation().shape
    
    def get_action_space_size(self):
        return self.simulation.get_player_ws().shape

    def compute_reward(self):
        # Penalize robot for getting out of field
        if not self.player_inside_field():
            return -500
        
        player_psi = self.simulation.get_player_psi()
        player_position = self.simulation.get_player_pos()
        player_ws = self.simulation.get_player_ws()
        player_v = np.linalg.norm(self.simulation.get_player_vs()[:2])
        lidar_read = self.simulation.get_player_lidar_read()

        angle_diff = abs(constrain_angle(player_psi - self.target_psi))
        max_angle_diff = np.pi
        angle_reward = -angle_diff/max_angle_diff

        dist = np.linalg.norm(player_position - self.target_position)
        max_dist = np.linalg.norm((WIDTH, HEIGHT))
        dist_reward = -dist/max_dist

        ws_diff_norm = np.linalg.norm(player_ws - self.previous_ws)
        max_ws_diff_norm = 4 * MAX_WHEEL_SPEED
        ws_reward = -ws_diff_norm/max_ws_diff_norm
    
        reward = dist_reward + 0.1 * angle_reward + 0.002 * ws_reward

        for read in lidar_read:
            if read < PLAYER_RADIUS:
                reward -= 1.2
        
        if dist < POSITION_TOLERANCE:
            reward += 0.05
        if angle_diff < ANGLE_TOLERANCE:
            reward += 0.01
        if player_v < VELOCITY_TOLERANCE:
            reward += 0.02

        if self.succesfull_finish():
            # Large bonus for reaching the desired state
            reward += 100
        
        return reward
    
    def succesfull_finish(self):
        player_position = self.simulation.get_player_pos()
        player_angle = self.simulation.get_player_psi()
        return (np.linalg.norm(player_position - self.target_position) < POSITION_TOLERANCE and
                abs(constrain_angle(player_angle - self.target_psi)) < ANGLE_TOLERANCE and
                np.linalg.norm(self.simulation.get_player_vs()[:2]) < VELOCITY_TOLERANCE)

    def player_inside_field(self):
        pos = self.simulation.get_player_pos()
        return ROBOT_MIN_WIDTH <= pos[0] <= ROBOT_MAX_WIDTH and ROBOT_MIN_HEIGHT <= pos[1] <= ROBOT_MAX_HEIGHT

    def check_done(self):
        # Stop episode if player is outside field
        if not self.player_inside_field():
            return True
        return self.succesfull_finish()

    def render(self, mode='human'):
        self.simulation.draw(np.concatenate((self.target_position, np.reshape(self.target_psi,(1,1)))))

    def close(self):
        self.simulation.close()
