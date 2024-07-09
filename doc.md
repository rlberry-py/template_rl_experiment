# Introduction
## Installation

To reproduce this experiment, we advise you use [pipenv](https://pipenv.pypa.io/) to create a virtual environment or just pip and virtualenv with the supplied versionning files in order to have the same version of python libraries as when the experiment was run by the authors.

**With pipenv**
```bash
cd empirical_rl/metadata
pipenv install
```

**With virtualenv and pip**
```bash
cd empirical_rl/metadata
pip install -r requirements.txt
```

## Skeleton of the experiment

We use scripts to write the experiment and not notebook because running large experiment in notebook is often not practical. 

# Experiment design
## Experiment code


%%% @python-src@empirical_rl/training.py

# Experiment results


