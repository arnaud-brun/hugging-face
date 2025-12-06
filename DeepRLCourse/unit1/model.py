import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.evaluation import evaluate_policy


# Create environment
# env = gym.make('LunarLander-v2')
env = make_vec_env('LunarLander-v2', n_envs=64)


# Instantiate the agent
model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 1024,
    batch_size = 64,
    n_epochs = 12,
    gamma = 0.999,
    gae_lambda = 0.98,
    ent_coef = 0.01,
    verbose=1)

# TODO: Train it for 1,000,000 timesteps => Downsized by factor 10
model.learn(total_timesteps=100000)

# TODO: Specify file name for model and save the model to file
model_name = "ppo-LunarLander-v2"
model.save(model_name)