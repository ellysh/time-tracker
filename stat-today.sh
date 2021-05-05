#!/bin/bash

set -e

REPORTS_DIR="csv"

./stat.py "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
