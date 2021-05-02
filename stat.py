#!/usr/bin/env python3

import sys
import csv
import time
import datetime

_USAGE = """Usage: stat.py <activity> <csv-file>
    activity - the string that describes your activity
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

def parse_lines(activity, reader):
  overall_time = 0

  for line in reader:
    if activity != get_value("Activity", line, _CSV_COLUMNS):
      continue

    overall_time += calculate_time(line)

    #print("{};{};{}".format(activity, get_value("Start_Time", line, _CSV_COLUMNS), \
    #      get_value("End_Time", line, _CSV_COLUMNS)))

  print("\nactivity = {} time = {} ({} s)".format(activity, str(datetime.timedelta(seconds=overall_time)), overall_time))

def show_statistics(activity, csv_file):
  with open(csv_file, "rU") as file_obj:
    reader = csv.reader(file_obj, delimiter=';')
    parse_lines(activity, reader)

def main():

  if len(sys.argv) == 3:
    activity = sys.argv[1]
    csv_file = sys.argv[2]
  else:
    print_usage(_USAGE)

  show_statistics(activity, csv_file)

if __name__ == '__main__':
  main()
