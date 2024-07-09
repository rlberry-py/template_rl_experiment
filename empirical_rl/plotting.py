from rlberry.manager import plot_writer_data, evaluate_agents
import pathlib
from rlberry.manager.experiment_manager import ExperimentManager
import matplotlib.pyplot as plt

default_ppo = "data_training_default_ppo"
path_to_load = next(
    pathlib.Path(default_ppo).glob("**/manager_obj.pickle")
)  # find the path to the "manager_obj.pickle"
loaded_experiment_manager_default_ppo = ExperimentManager.load(path_to_load) 


avec_ppo = "data_training_avec_ppo"
path_to_load = next(
    pathlib.Path(avec_ppo).glob("**/manager_obj.pickle")
)  # find the path to the "manager_obj.pickle"
loaded_experiment_manager_avec_ppo = ExperimentManager.load(path_to_load) 



_ = plot_writer_data([loaded_experiment_manager_default_ppo, loaded_experiment_manager_avec_ppo],
    tag="rollout/ep_rew_mean",
    title="Training Episode Cumulative Rewards",
    show=False,
    savefig_fname="rewards"
)

_ = plot_writer_data([loaded_experiment_manager_default_ppo, loaded_experiment_manager_avec_ppo],
    tag="train/explained_variance",
    title="Training Explained Variance",
    show=False,
    savefig_fname="explained_variance"
)


_ = plot_writer_data([loaded_experiment_manager_default_ppo, loaded_experiment_manager_avec_ppo],
    tag="train/value_loss",
    title="Training Value Loss",
    show=False,
    savefig_fname="value_loss"
)

_ = evaluate_agents(
    [loaded_experiment_manager_default_ppo, loaded_experiment_manager_avec_ppo], n_simulations=50, show=False,
)  # Evaluate the trained agent on
plt.savefig("evaluations")

