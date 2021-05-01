#!/bin/bash -x

set -e

./tracker.py work >> "$(date +%Y-%m-%d).csv"
