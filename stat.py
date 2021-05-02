#!/usr/bin/env python3

import sys
import csv
import time
import datetime

_USAGE = """Usage: stat.py <csv-file>
    csv-file - the CSV file with statistics

Example:
    stat.py work 2021-05-01.csv
"""

_CSV_COLUMNS = {
    "Activity" : 0,
    "Start_Time" : 1,
    "End_Time" : 2
}

def print_usage(usage):
  sys.stderr.write(usage)
  sys.exit(1)

def get_value(key, input_line, columns):
  return input_line[columns[key]]

def calculate_time(line):
  return float(get_value("End_Time", line, _CSV_COLUMNS)) \
         - float(get_value("Start_Time", line, _CSV_COLUMNS))

def parse_lines(reader):
  overall_time = 0

  statistics = {}

  for line in reader:
    activity = get_value("Activity", line, _CSV_COLUMNS)

    if activity in statistics:
      statistics[activity] += calculate_time(line)
    else:
      statistics[activity] = calculate_time(line)

  for activity, overall_time in sorted(statistics.items()):
    print("\nThe activity \"{}\" took {} ({} s)".format(activity, str(datetime.timedelta(seconds=overall_time)), overall_time))

def show_statistics(csv_file):
  with open(csv_file, "rU") as file_obj:
    reader = csv.reader(file_obj, delimiter=';')
    parse_lines(reader)

def main():

  if len(sys.argv) == 2:
    csv_file = sys.argv[1]
  else:
    print_usage(_USAGE)

  show_statistics(csv_file)

if __name__ == '__main__':
  main()
