from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit
from torch.nn import ReLU

import argparse

MAX_EPISODE_STEPS = 1024
TOTAL_TIMESTEPS = 2**25

def train(render, total_timesteps, max_episode_steps):
    # Initialize the environment
    env = CustomEnv(render=render)
    env = TimeLimit(env, max_episode_steps= max_episode_steps)

    arch = [64, 64]
    policy_kwargs = {'activation_fn':ReLU, 'net_arch':arch}
    # Initialize the PPO agent
    model = PPO('MlpPolicy',
                env, 
                verbose=1, 
                batch_size=2**10, 
                device="cpu", 
                tensorboard_log="./ssl_tensorboard/", 
                policy_kwargs=policy_kwargs)

    # Train the agent
    model.learn(total_timesteps=total_timesteps, progress_bar=True)  # Adjust the timesteps as needed

    # Save the model
    model.save("ssl_model")

    print("Finished training")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--render', action='store_true', help="Render the environment if this flag is set.")

    parser.add_argument('--max_episode_steps', type=int, default=MAX_EPISODE_STEPS, help="Maximum number of steps per episode.")
    
    parser.add_argument('--total_timesteps', type=int, default=TOTAL_TIMESTEPS, help="Total number of timesteps to run the environment.")

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the main function with the render argument
    train(render=args.render, max_episode_steps=args.max_episode_steps, total_timesteps=args.total_timesteps)