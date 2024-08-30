from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv

# render = True
render = False

# Initialize the environment
env = CustomEnv(render=render)

# Initialize the PPO agent
model = PPO('MlpPolicy', env, verbose=1, device="cuda")

# Train the agent
model.learn(total_timesteps=8000000, progress_bar=True)  # Adjust the timesteps as needed

# Save the model
model.save("ssl_model")

print("Finished training")