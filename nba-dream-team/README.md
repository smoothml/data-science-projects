# NBA Dream Team

## Objective
We're looking to get a feel for core problem-solving skills. The prompt is intentionally open-ended for interpretation. Based on the open nature of the prompt, this assignment could take as little as 10 minutes and on the flip side, it could merit 10's of hours. Please target to spend 2-3 hours on the assignment after loading the dataset into a notebook. To reiterate, one of the main purposes 
of the open prompt is to allow for creativity and interpretation - if you can defend it, there are no wrong answers. Having fun with this assignment isn't the worst thing in the world.

## Prompt
Based on the dataset, create your "best" 5 person dream team with 1 player in each of their respective positions (PG, SG, SF, PF, C). Caveat - you can only use 1 player per decade and within the past 5 decades (aka - 2010's, 2000's, 1990's, 1980's, 1970's). If a player has played at least 1 game in multiple decades, you can use them for whichever decade you prefer.

Once your rockstar team is assembled, predict the number of points they will score in the upcoming season.

## Evaluation
As mentioned and with nature of the prompt, we're looking to evaluate the assignment based on 1) the ability to produce a clean problem statement/strategy, 2) creativity of strategy, 3) quality of code, 4) ability to communicate results and insights worth exploring in the future.

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
nba-dream-team
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
    ├ nba_dream_team
    │   └ __init__.py
    ├ tests
    │   └ __init__.py
    └ setup.py
```
Project based on the [DataBake](https://github.com/smoothml/data-bake) template.
