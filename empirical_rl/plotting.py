from rlberry.manager import plot_writer_data


# aliases for exp results 
default_ppo = "/data_training_default_ppo/manager_data/ppo-default_2024-07-03_11-26-14_b0045e63/agent_handlers/"
avec_ppo = "data_training_avec_ppo/manager_data/avec-ppo_2024-07-03_11-26-14_9e4b15e4/"

_ = plot_writer_data([default_ppo, avec_ppo],
    tag="rollout/ep_rew_mean",
    title="Training Episode Cumulative Rewards",
    show=False,
    savefig_fname="rewards"
)

_ = plot_writer_data([default_ppo, avec_ppo],
    tag="train/explained_variance",
    title="Training Explained Variance",
    show=False,
    savefig_fname="explained_variance"
)


_ = plot_writer_data([default_ppo, avec_ppo],
    tag="train/value_loss",
    title="Training Value Loss",
    show=False,
    savefig_fname="value_loss"
)

