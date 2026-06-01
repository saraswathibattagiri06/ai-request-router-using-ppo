import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AIRouterEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):

        self.state = np.random.rand(4)

        return self.state, {}

    def step(self, action):

        complexity = self.state[0]

        costs = [0.8, 0.6, 0.4, 0.2]
        quality = [0.95, 0.85, 0.75, 0.60]

        reward = quality[action] * complexity - costs[action]

        self.state = np.random.rand(4)

        terminated = False
        truncated = False

        return self.state, reward, terminated, truncated, {}