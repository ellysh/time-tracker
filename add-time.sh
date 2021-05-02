#!/bin/bash

set -e

ACTIVITY="$1"
TIME="$2"
REPORTS_DIR="csv"

./add-time.py "$ACTIVITY" "$TIME" >> "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
