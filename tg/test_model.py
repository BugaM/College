from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv

# Initialize the environment
env = CustomEnv(render=True)

model = PPO.load("ssl_model")

# Test the trained agent
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()