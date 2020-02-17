# MNIST Classifier

Hand written digit classifier using the MNIST dataset.

## Requirements
* [GNU Make](https://www.gnu.org/software/make/)
* Python 3.7 or above

## Usage
### `make` commands

| Command                   | Description |
| ------------------------- | ----------- |
| `make environment` | Create a [Python virtual environment](https://docs.python-guide.org/dev/virtualenvs/). |
| `make clean` | Remove Python virtual environment. |
| `make lint` | Run [Flake8](https://flake8.pycqa.org) linting. |
| `make test` | Run tests with [PyTest](https://pytest.org). |

## Project Structure
```
mnist-classifier
├ Makefile              <- Makefile with helpful make commands.
├ README.md             <- Top-level README for project developers.
├ .env                  <- Secrets. DO NOT SOURCE CONTROL!
├ .gitignore            <- Files to ignore.
├ pytest.ini            <- PyTest configuration.
├ setup.cfg             <- Project configuration.
├ data
│   ├ external          <- Data from external sources.
│   ├ interim           <- Intermediate, transformed data.
│   ├ processed         <- Final, canonical data sets from modelling.
│   ├ raw               <- Original, immutable raw data sets.
│   ├ results           <- Results of modelling and analysis.
│   └ resources         <- Useful resources (e.g. relevant papers).
├ models                <- Trained and serialized models, model predictions, or model summaries.
├ notebooks             <- Jupyter notebooks.
├ outputs               <- Generated outputs, such as figures or reports.
├ requirements.txt      <- Python requirements file for reproducing the analysis environment.
└ src                   <- Source code for use in the project comprising a Python package and tests.
    ├ mnist_classifier
    │   └ __init__.py
    ├ tests
    │   └ __init__.py
    └ setup.py
```
Project based on the [DataBake](https://github.com/smoothml/data-bake) template.
