from rlberry.manager import evaluate_agents
import matplotlib.pyplot as plt


# aliases for exp results 
avec_ppo = "rlberry_data/temp/manager_data/avec-ppo_2024-07-03_11-09-17_06970bd6"
default_ppo = "rlberry_data/temp/manager_data/avec-ppo_2024-07-03_11-09-17_06970bd6"
_ = evaluate_agents(
    [default_ppo, avec_ppo], n_simulations=50, show=False,
)  # Evaluate the trained agent on
plt.savefig("evaluations")

