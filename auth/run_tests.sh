#!/usr/bin/env bash

python -m unittest discover -s test.unit -p "Test*.py" -t . &&
python -m unittest discover -s test.functional -p "Functional*.py" -t .