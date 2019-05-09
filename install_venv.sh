#!/usr/bin/env bash

set -o errexit

ENV_DIR=".venv"

hash virtualenv 2>/dev/null || { echo >&2 "Virtualenv is not installed.  Aborting."; exit 1; }
rm -rf ${ENV_DIR}

echo "--> Installing venv directory"
virtualenv --python=python3 ${ENV_DIR}
source ${ENV_DIR}/bin/activate
pip install -r requirements.txt
