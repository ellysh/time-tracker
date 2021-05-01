#!/bin/bash

set -e

ACTIVITY="work"
REPORTS_DIR="csv"

./tracker.py "$ACTIVITY" >> "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
