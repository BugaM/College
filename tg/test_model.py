from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit

# Initialize the environment
env = CustomEnv(render=True)
env = TimeLimit(env, max_episode_steps=500)
model = PPO.load("ssl_model")

# Test the trained agent
obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()