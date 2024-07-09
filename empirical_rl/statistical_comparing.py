from rlberry.manager import AdastopComparator
from rlberry.agents.stable_baselines import StableBaselinesAgent
from rlberry.envs import gym_make
from rlberry.seeding import Seeder

from stable_baselines3 import PPO
from avec_ppo import AVECPPO


seed = Seeder(42)

managers = [
dict(
    agent_class=StableBaselinesAgent,  # The Agent class.
    train_env=(gym_make, dict(id="Acrobot-v1")),  # The Environment to solve.
    fit_budget=5e4,  # The number of interactions
    # between the agent and the
    # environment during training.
    init_kwargs=dict(algo_cls=PPO),  # Init value for StableBaselinesAgent
    eval_kwargs=dict(eval_horizon=500),  # The number of interactions
    # between the agent and the
    # environment during evaluations.
    agent_name="default_ppo",  # The agent's name.
),
dict(
    agent_class = StableBaselinesAgent,  # The Agent class.
    train_env=(gym_make, dict(id="Acrobot-v1")),  # The Environment to solve.
    fit_budget=5e4,  # The number of interactions
    # between the agent and the
    # environment during training.
    init_kwargs=dict(algo_cls=AVECPPO),  # Init value for StableBaselinesAgent
    eval_kwargs=dict(eval_horizon=500),  # The number of interactions
    # between the agent and the
    # environment during evaluations.
    agent_name="avec_ppo",  # The agent's name.
) ]
# # Comparing distributions
comparator = AdastopComparator(seed=42)
comparator.compare(managers)
print(comparator.managers_paths)
