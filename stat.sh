#!/bin/bash

set -e

ACTIVITY="work"
REPORTS_DIR="csv"

./stat.py "$ACTIVITY" "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
