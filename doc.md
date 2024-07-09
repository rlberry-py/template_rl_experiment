# Introduction
## Installation

To reproduce this experiment, you can either use pip and virtualenv or you can use [pipenv](https://pipenv.pypa.io/) to create a virtual environment with the supplied versionning files in order to have the same version of python libraries as when the experiment was run by the authors. Remark that pipenv can be long to run but is more precise in its versionning of python libraries.

**With virtualenv and pip**
```bash
python -m venv rlberry_xp_venv
source rlberry_xp_venv/bin/activate
cd empirical_rl/metadata
pip install -r requirements.txt
```

**With pipenv**
```bash
cd empirical_rl/metadata
pipenv install
pipenv shell
```


## Skeleton of the experiment

We use scripts to write the experiment and not notebook because running large experiment in notebook is often not practical. 

# Experiment design
## Experiment code


%%% @python-src@empirical_rl/training.py

# Experiment results


