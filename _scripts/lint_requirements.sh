#!/bin/bash
# Make sure requirements.txt are in sync with Pipfile.lock

set -e

add_slash_re='s#pypi.org/simple/*$#pypi.org/simple/#'
remove_comment_re='s# *;.*##'

cat requirements.txt | sed -e "$add_slash_re" | sed -e "$remove_comment_re" > normalized-requirements.txt
pipenv lock --requirements | sed -e "$add_slash_re" | sed -e "$remove_comment_re" > just-locked-requirements.txt

if ! diff normalized-requirements.txt just-locked-requirements.txt
then
  rm *-requirements.txt
  help_url='https://docs.pyvec.org/CONTRIBUTING.html#zavislosti'
  echo ""
  echo ""
  echo "The requirements.txt file is not up to date. Run" \
    "'pipenv lock --requirements > requirements.txt' and commit changes." \
    "See ${help_url} for more info."
  exit 1
else
  rm *-requirements.txt
fi
