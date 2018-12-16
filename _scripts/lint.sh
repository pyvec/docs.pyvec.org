#!/bin/bash
set -e

# Lint Python code
pipenv run pylama

# Make sure requirements.txt are in sync with Pipfile.lock
pipenv run pipenv_to_requirements -f -o ci-requirements.txt
if ! diff requirements.txt ci-requirements.txt > /dev/null
then
  rm ci-requirements.txt
  help_url='https://pyvec-guide.readthedocs.io/CONTRIBUTING.html#zavislosti'
  echo ""
  echo ""
  echo "The requirements.txt file is not up to date. Run" \
    "'pipenv run requirements' and commit the changes." \
    "See ${help_url} for more info."
  exit 1
else
  rm ci-requirements.txt
fi

# Check external links
pipenv run sphinx-build -nW -b linkcheck . _build
