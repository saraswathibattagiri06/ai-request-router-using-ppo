from stable_baselines3 import PPO
from env import AIRouterEnv

env = AIRouterEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=20000
)

model.save("models/ppo_router")