.PHONY: environment clean lint test get-data

#################################################################################
# COMMANDS                                                                      #
#################################################################################

environment: ## Create Python virtual environment and install dependencies.
	@echo "Creating environment..."
	@python3 -m venv venv
	@( \
		. venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r requirements.txt;\
	)

clean: ## Clean environment.
	@rm -rf venv .pytest_cache

lint: ## Lint source code.
	@flake8 src/nba_dream_team

test: ## Run tests.
	@pytest

get-data: ## Download data.
	@kaggle datasets download -p data/raw drgilermo/nba-players-stats
	@unzip -o data/raw/*.zip -d data/raw
	@rm data/raw/*.zip

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
