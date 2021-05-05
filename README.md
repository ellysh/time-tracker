# Time Tracker 0.1v

This is an elementary time tracking system. It stores statistics of your activities in CSV format. You can retrieve this statistic for each specific date.

## Requirements

You need Bash and Python 3 interpreters to launch the scripts.

## Usage

### Tracking Activity

Here is an example to launch the tracker script:
```bash
./tracker.py work >> "csv/$(date +%Y-%m-%d).csv"
```

The "work" parameter means the name for your activity.

When you are done with your activity, interrupt the script by the Ctrl+C shortcut. When you come back to your activity, start the script again. It will accumulate your workflow in the specified CSV file.

Another option is to use the Bash wrapper instead of the `tracker.py` script. Run the wrapper this way:
```bash
./tracker-today.sh "work"
```

Stop the wrapper by the Ctrl+C shortcut too.

The wrapper stores CSV reports in the `csv` subdirectory.

You can change the activity name and the path for reports in the `tracker.sh` wrapper. Specify these parameters in the `ACTIVITY` and `REPORTS_DIR` variables there.

### Adding Time Manually

You can add time to the CSV report manually. Use the `add-time.py` script for that. Call the script this way:
```bash
./add-time.py work 2h >> "csv/$(date +%Y-%m-%d).csv"
```

The alternative option is using the Bash wrapper like this:
```bash
add-time-today.sh work 2h
```

### Retrieving Statistic

Here is an example to retrieve statistics for the current date:
```bash
./stat.py "csv/$(date +%Y-%m-%d).csv"
```

It shows the overall time you spent for each activity in this day.

The Bash wrapper shows you statistics for today. Run it this way:
```bash
./stat-today.sh
```

You can change the path to CSV reports in the `REPORTS_DIR` variables there.

## Contacts

If you have suggestions, bug reports or questions about Time Tracker usage, please contact me via email petrsum@gmail.com.
