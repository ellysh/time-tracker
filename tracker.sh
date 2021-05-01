#!/bin/bash

set -e

REPORTS_DIR="csv"

./tracker.py work >> "$REPORTS_DIR/$(date +%Y-%m-%d).csv"
