# ABM Coursework - EPGP17 - IIMK

This repository contains the agents built for the ABM coursework. Each model is enclosed in a directory with the prefix `M`.

## Getting started

Install Python 3.12 from <https://www.python.org/downloads/>

Install git from <https://git-scm.com/install/>

Install UV from <https://docs.astral.sh/uv/getting-started/installation/>

```shell
git clone https://github.com/subinabid/ABMCourseWork.git
cd ABMCoursework
uv sync
```

`uv sync` will install all required dependencies like `igraph` and `mathplotlib`

## Running the models

Models are stored in directories names with an `M` prefix like `M1opiniondynamics`

Each model has the following files

- `agents.py` -> defining the agent(s)
- `parameters.py` -> parameters of the model
- `environment.py` -> the interaction rules and
- `model.py` -> which runs the model itself
  
Run the model with uv. Example:

```shell
uv run python M1opiniondynamics/model.py
```