from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback

from torch.nn import ReLU

import argparse

MAX_EPISODE_STEPS = 512
TOTAL_TIMESTEPS = 2**26 + 2**25


def train(render, total_timesteps, max_episode_steps):
    # Initialize the environment
    vec_env = make_vec_env(lambda: TimeLimit(CustomEnv(render, seed=42, num_opps=5), max_episode_steps=max_episode_steps), n_envs=32)

    policy_kwargs = dict(
        activation_fn=ReLU,
        net_arch=dict(pi=[256, 256], vf=[256, 256])
    )
    # Initialize the PPO agent
    model = PPO('MlpPolicy',
                vec_env, 
                verbose=1, 
                n_steps=2048,
                batch_size=512, 
                n_epochs=15,
                gamma=0.99,
                ent_coef=1e-5,
                clip_range=0.2,
                learning_rate=5e-5,
                seed=42,
                device="cuda", 
                tensorboard_log="./ssl_tensorboard/", 
                policy_kwargs=policy_kwargs)
    
    eval_env = make_vec_env(lambda: TimeLimit(CustomEnv(render=False, seed=10, num_opps=5), max_episode_steps=max_episode_steps), n_envs=1)

    # Set up EvalCallback
    eval_callback = EvalCallback(eval_env, 
                                 best_model_save_path='./noised_model/',
                                 log_path='./noised_model/',
                                 eval_freq=10000,  # Evaluate every 10000 timesteps
                                 deterministic=True, 
                                 render=False)

    # Train the agent
    model.learn(total_timesteps=total_timesteps, progress_bar=True, callback=eval_callback)  # Adjust the timesteps as needed

    # Save the model
    model.save("ssl_model_noised_2")

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