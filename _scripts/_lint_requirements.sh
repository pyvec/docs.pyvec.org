#!/bin/bash
set -e

# Make sure requirements.txt are in sync with Pipfile.lock
pipenv lock --requirements | sed -e 's#pypi.org/simple$#pypi.org/simple/#' > ci-requirements.txt
if ! diff requirements.txt ci-requirements.txt > /dev/null
then
  rm ci-requirements.txt
  help_url='https://pyvec-guide.readthedocs.io/CONTRIBUTING.html#zavislosti'
  echo ""
  echo ""
  echo "The requirements.txt file is not up to date. Run" \
    "'pipenv lock --requirements > requirements.txt' and commit changes." \
    "See ${help_url} for more info."
  exit 1
else
  rm ci-requirements.txt
fi
