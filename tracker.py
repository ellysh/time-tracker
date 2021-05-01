#!/usr/bin/env python3

import sys
import time

_USAGE = """Usage: tracker.py <activity>
    activity - the string that describes your activity

Example:
    tracker.py work
"""

def print_usage(usage):
  sys.stderr.write(usage)
  sys.exit(1)

def write_time_to_csv(activity, start_time):
  end_time = time.time()

  print("activity = {} start_time = {} end_time = {}".format(activity, start_time, end_time))

def track_activity(activity):
  start_time = time.time()

  try:
    while True:
      time.sleep(0.5)

  except KeyboardInterrupt:
    write_time_to_csv(activity, start_time)

def main():

  if len(sys.argv) == 2:
    activity = sys.argv[1]
  else:
    print_usage(_USAGE)

  track_activity(activity)

if __name__ == '__main__':
  main()
