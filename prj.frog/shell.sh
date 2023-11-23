#!/usr/bin/env bash

#------------------------------------------------------------------
# Go to the directory containing this script.

cd $(dirname $0)

#------------------------------------------------------------------
# Install the virtual environment

python3 -m venv ./.venv

#------------------------------------------------------------------
# Activate the virtual environment.

source ./.venv/bin/activate 

#------------------------------------------------------------------
# Have [pip] upgrade itself to the latest version.

pip install --upgrade pip

#------------------------------------------------------------------
# Have it install all packages listed in [./requirements.txt].

pip install -r ./requirements.txt

#------------------------------------------------------------------
# One of the packages is [pytest].  Run it to test our frog game.

pytest

#------------------------------------------------------------------
# Finally, launch a bash shell so we can play with our game.

bash
