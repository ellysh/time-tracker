# Time Tracker 0.1v

This is an elementary time tracking system. It stores statistics of your activities in CSV format. Than you can retrieve the statistic for each specific date.

## Requirements

You need Bash and Python 3 interpreters to launch the scripts.

## Usage

### Tracking Activity

Here is an example to launch the tracker script:
```bash
./tracker.py work >> "csv/$(date +%Y-%m-%d).csv"
```

The `work` means the name for your activity.

When you are done with your activity, interrupt the script by the Ctrl+C shortcut.

Another option is to use the Bash wrapper:
```bash
./tracker.sh
```

Stop the wrapper by the Ctrl+C shortcut too.

The wrapper stores CSV reports in the "csv" subdirectory.

You can change the activity name and the path for reports in the `tracker.sh` script. Specify these parameters in the `ACTIVITY` and `REPORTS_DIR` variables there.

### Retrieving Statistic

Here is an example to retrieve statistics for the current date:
```bash
./stat.py work "csv/$(date +%Y-%m-%d).csv"
```

It shows the time you spent doing the `work` activity.

The same data you can retrieve with the Bash wrapper:
```bash
./stat.sh
```
