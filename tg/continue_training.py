from stable_baselines3 import PPO
from reinforcement_learning.environment import CustomEnv
from gym.wrappers.time_limit import TimeLimit
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback


from torch.nn import ReLU

import argparse



MAX_EPISODE_STEPS = 512
TOTAL_TIMESTEPS = 2**24


def continue_training(render, total_timesteps, max_episode_steps, model_path="ssl_model_noised_2", log_path="ssl_model_noised_2"):
    # Initialize the environment
    vec_env = make_vec_env(lambda: TimeLimit(CustomEnv(render, seed=42, num_opps=5), max_episode_steps=max_episode_steps), n_envs=32)
    # Initialize the PPO agent
    model = PPO.load(model_path, tensorboard_log=log_path)
    model.set_env(vec_env)

    eval_env = make_vec_env(lambda: TimeLimit(CustomEnv(render=False, seed=10, num_opps=5), max_episode_steps=max_episode_steps), n_envs=1)
    eval_path = "./noised_model_2_continued/"
    # Set up EvalCallback
    eval_callback = EvalCallback(eval_env, 
                                 best_model_save_path=eval_path,
                                 log_path=eval_path,
                                 eval_freq=10000,  # Evaluate every 10000 timesteps
                                 deterministic=True, 
                                 render=False)
    # Train the agent
    model.learn(total_timesteps=total_timesteps, reset_num_timesteps=False, tb_log_name="continued", progress_bar=True, callback=eval_callback)  # Adjust the timesteps as needed

    # Save the model
    model.save("ssl_noised_model_2_continued")

    print("Finished training")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--render', action='store_true', help="Render the environment if this flag is set.")

    parser.add_argument('--max_episode_steps', type=int, default=MAX_EPISODE_STEPS, help="Maximum number of steps per episode.")
    
    parser.add_argument('--total_timesteps', type=int, default=TOTAL_TIMESTEPS, help="Total number of timesteps to run the environment.")

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the main function with the render argument
    continue_training(render=args.render, max_episode_steps=args.max_episode_steps, total_timesteps=args.total_timesteps)