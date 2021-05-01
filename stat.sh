#!/bin/bash -x

set -e

REPORTS_DIR="csv"

./stat.py work "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
