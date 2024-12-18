from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit
import time
from utils import constrain_angle
from constants.simulation_constants import DELTA_T, RL_STEPS
from constants.robot_constants import POSITION_TOLERANCE, ANGLE_TOLERANCE, VELOCITY_TOLERANCE, MAX_WHEEL_SPEED, MAX_VELOCITY, MAX_ANGULAR, MAX_ACC
import numpy as np

GET_HISTORY = True

# Initialize the environment
env = CustomEnv(render=True, num_opps=10, seed = 20, draw_lidar=True, get_histoy=GET_HISTORY)
env = TimeLimit(env, max_episode_steps=510)
model = PPO.load("ssl_model_noised_2 copy", env)
# model = PPO.load("ssl_model_noised", env)

# Test the trained agent
obs = env.reset()
episode = 0
while True:
    start = time.time()
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    dist = np.linalg.norm(env.simulation.get_player_pos() - env.target_position)
    angle_diff = abs(constrain_angle(env.simulation.get_player_psi() - env.target_psi))
    speed_diff = np.linalg.norm(env.simulation.get_player_vs()[:2])
    # print(env.simulation.get_player_lidar_read())
    # print( np.linalg.norm(env.simulation.get_player_vs()[:2]))
    # print(f'DIST: {dist}, DIST < TOL: {dist < POSITION_TOLERANCE}')
    # print(f'ANGLE_DIFF: {angle_diff}, ANGLE_DIFF < TOL: {angle_diff < ANGLE_TOLERANCE}')
    # print(f'SPEED_DIFF: {speed_diff}, SPEED_DIFF < TOL: {speed_diff < VELOCITY_TOLERANCE}')
    # env.render()
    while True:
        if time.time() - start >= RL_STEPS * DELTA_T:
            break
    if done:
        episode +=1
        print( np.linalg.norm(env.simulation.get_player_vs()[:2]))
        print( env.simulation.get_player_vs())
        print( env.simulation.get_player_ws())
        if episode <= 3:
            env.simulation.draw_ws_graphs(name=f"episode_{episode}_ws")
        obs = env.reset()

env.close()