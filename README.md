# Adaptive AI Request Router using Reinforcement Learning

## Overview

Adaptive AI Request Router is a reinforcement learning project that simulates intelligent routing decisions across multiple AI service providers. The objective is to maximize utility while minimizing operational costs by learning an optimal routing policy using Proximal Policy Optimization (PPO).

The project models a simplified AI infrastructure environment where requests with varying complexity are routed to different providers with different cost and quality characteristics. The PPO agent learns to make routing decisions that balance response quality and resource expenditure.

---

## Problem Statement

Modern AI systems often have access to multiple model providers with varying:

* Inference cost
* Response quality
* Latency characteristics

Selecting the most appropriate provider for each request is a sequential decision-making problem.

This project explores whether a reinforcement learning agent can learn a routing strategy that outperforms simple heuristic approaches such as random selection and ε-greedy exploration.

---

## Features

* Custom Gymnasium environment
* PPO-based routing agent using Stable-Baselines3
* Cost-aware reward optimization
* Simulated AI provider selection
* Performance visualization
* Baseline comparison using Multi-Armed Bandit strategies

---

## Environment Design

### State Space

The environment provides a four-dimensional state vector representing:

* Request complexity
* Available budget indicator
* Queue depth indicator
* Historical success metric

### Action Space

The agent selects one of four available providers:

| Action | Provider   |
| ------ | ---------- |
| 0      | Provider A |
| 1      | Provider B |
| 2      | Provider C |
| 3      | Provider D |

### Reward Function

The reward balances service quality against operational cost:

Reward = Quality Score × Request Complexity − Cost Penalty

The objective is to maximize cumulative reward over time.

---

## Project Structure

```text
ai-request-router/

├── env.py
├── train_ppo.py
├── evaluate.py
├── bandits.py
├── requirements.txt
├── README.md

├── models/

└── results/
```

---

## Technologies Used

* Python
* Gymnasium
* Stable-Baselines3
* PyTorch
* NumPy
* Pandas
* Matplotlib

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-request-router.git

cd ai-request-router
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training

Train the PPO agent:

```bash
python train_ppo.py
```

The trained model will be saved inside:

```text
models/
```

---

## Evaluation

Evaluate the trained policy:

```bash
python evaluate.py
```

Generated plots will be stored inside:

```text
results/
```

---

## Results

The PPO agent learns routing policies that adapt to changing request complexity and provider trade-offs.

Evaluation metrics include:

* Average reward
* Cumulative reward
* Provider selection distribution
* Reward trends over time

Future versions will include:

* UCB Baseline
* Thompson Sampling
* Regret Analysis
* Budget-Constrained Routing
* Contextual Bandits
* Sim-to-Real Validation

---

## Future Work

* Implement Upper Confidence Bound (UCB) routing
* Add Thompson Sampling baseline
* Introduce latency-aware rewards
* Build contextual bandit variants
* Compare PPO against DQN and A2C
* Support real API cost and quality metrics
* Deploy policy as a routing microservice

---

## Resume Impact

This project demonstrates:

* Reinforcement Learning fundamentals
* PPO implementation
* Reward engineering
* Exploration vs Exploitation strategies
* Custom environment design
* Performance evaluation and visualization
* Applied optimization for AI infrastructure

---

## Author

Saraswathi Battagiri

Electronics & Instrumentation Engineering
Applied AI | Machine Learning | Reinforcement Learning | GenAI Systems
