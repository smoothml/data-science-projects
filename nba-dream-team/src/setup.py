import re
from pathlib import Path
from setuptools import find_packages, setup

NAME = 'nba-dream-team'
DESCRIPTION = 'A short description of the project.'
REQUIRES_PYTHON = '>=3.5.0'
AUTHOR = 'Paul Harrison'

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'nba_dream_team'

# Get package version
VERSION = '0.0.1' # Default version
version_pattern = re.compile("(?<=__version__\s=\s['\"])\d\.\d\.?\d?")
with open(PACKAGE_DIR / '__init__.py') as f:
    for line in f:
        res = version_pattern.search(line.strip())
        if res is not None:
            VERSION = res.group(0)

REQUIREMENTS = []

setup(
    name=NAME,
    packages=find_packages(exclude=['tests']),
    version=VERSION,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    author=AUTHOR
)
