#!/usr/bin/env python3

import sys
import time

_USAGE = """Usage: add-time.py <activity> <time>
    activity - the string that describes your activity
    time - the time in minutes you spent doing the activity

Examples:
    add-time.py work 30m
    add-time.py work 1.5h
"""

def print_usage(usage):
  sys.stderr.write(usage)
  sys.exit(1)

def write_time_to_csv(activity, start_time, end_time):
  print("{};{};{}".format(activity, start_time, end_time))

def str_to_seconds(t):
  time_units = t[-1]
  time_value = t[:-1]

  if time_units == 'm':
    return float(time_value) * 60
  elif time_units == 'h':
    return float(time_value) * 3600
  else:
    return 0

def add_time(activity, add_time):
  start_time = time.time()

  write_time_to_csv(activity, start_time, start_time + str_to_seconds(add_time))

def main():

  if len(sys.argv) == 3:
    activity = sys.argv[1]
    time = sys.argv[2]
  else:
    print_usage(_USAGE)

  add_time(activity, time)

if __name__ == '__main__':
  main()
