#!/bin/bash

# Get the path to this file's directory.
OUTPUT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

pybind11-stubgen pyslang -o $OUTPUT_DIR --root-suffix ''
