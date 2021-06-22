#!/bin/bash

# forget other commands
set -e

# ensure that the script has been sourced rather than just executed
if [[ "${BASH_SOURCE[0]}" = "${0}" ]]; then
    echo "ERROR: run '$ source setup.sh'"
    exit 1
fi

# create conda environment and activate that
conda env create -f environment.yml || true
conda activate $(grep 'name:' environment.yml | awk '{print $NF}')

set +e
return 