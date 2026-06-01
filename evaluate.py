from stable_baselines3 import PPO
from env import AIRouterEnv
import matplotlib.pyplot as plt

env = AIRouterEnv()

model = PPO.load("models/ppo_router")

rewards = []

obs, _ = env.reset()

for _ in range(1000):

    action, _ = model.predict(obs)

    obs, reward, _, _, _ = env.step(action)

    rewards.append(reward)

plt.plot(rewards)
plt.title("PPO Rewards")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.savefig("results/ppo_rewards.png")
plt.show()