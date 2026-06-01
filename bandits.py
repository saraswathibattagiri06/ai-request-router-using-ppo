import random
import numpy as np

class EpsilonGreedy:

    def __init__(self):

        self.epsilon = 0.1

    def choose(self):

        if random.random() < self.epsilon:
            return random.randint(0,3)

        return 0