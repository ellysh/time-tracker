#!/bin/bash

set -e

ACTIVITY="$1"
REPORTS_DIR="csv"

./tracker.py "$ACTIVITY" >> "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
