#!/bin/bash

set -e

#ACTIVITY="work"
ACTIVITY="writing"
REPORTS_DIR="csv"

./stat.py "$ACTIVITY" "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
