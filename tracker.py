#!/usr/bin/env python3

import time

_USAGE = """Usage: tracker.py <activity>
    activity - the string that describes your activity

Example:
    tracker.py work
"""

def write_time_to_csv(start_time):
  end_time = time.time()

  print("start_time = {} end_time = {}".format(start_time, end_time))

def main():
  start_time = time.time()

  try:
    while True:
      time.sleep(0.5)

  except KeyboardInterrupt:
    write_time_to_csv(start_time)

if __name__ == '__main__':
  main()
