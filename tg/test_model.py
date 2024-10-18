from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit
import time
from utils import constrain_angle
from constants.simulation_constants import DELTA_T
from constants.robot_constants import POSITION_TOLERANCE, ANGLE_TOLERANCE, VELOCITY_TOLERANCE, MAX_WHEEL_SPEED, MAX_VELOCITY, MAX_ANGULAR, MAX_ACC
import numpy as np

# Initialize the environment
env = CustomEnv(render=True, num_opps=5, seed = 18)
env = TimeLimit(env, max_episode_steps=510)
model = PPO.load("ssl_model_continued")

# Test the trained agent
obs = env.reset()
while True:
    start = time.time()
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    dist = np.linalg.norm(env.simulation.get_player_pos() - env.target_position)
    angle_diff = abs(constrain_angle(env.simulation.get_player_psi() - env.target_psi))
    speed_diff = np.linalg.norm(env.simulation.get_player_vs()[:2])
    print(f'DIST: {dist}, DIST < TOL: {dist < POSITION_TOLERANCE}')
    print(f'ANGLE_DIFF: {angle_diff}, ANGLE_DIFF < TOL: {angle_diff < ANGLE_TOLERANCE}')
    print(f'SPEED_DIFF: {speed_diff}, SPEED_DIFF < TOL: {speed_diff < VELOCITY_TOLERANCE}')
    env.render()
    while True:
        if time.time() - start >= DELTA_T:
            break
    if done:
        obs = env.reset()

env.close()