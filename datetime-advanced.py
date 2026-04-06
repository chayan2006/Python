# ⏰ Advanced Datetime: Timezones, Deltas, and Formatting

from datetime import datetime, date, timedelta
import time

# 1. Date and Time Formatting (strftime)
# %Y: Year (2024), %m: Month (01 to 12), %d: Day (01 to 31)
# %H: Hour (00 to 23), %M: Minute (00 to 59), %S: Second (00 to 59)
now = datetime.now()
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 2. String to Datetime object (strptime)
# Example: Parsing a date from a text file or user input
date_str = "2024-03-31 15:45:00"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Object:", dt_obj)

# 3. Arithmetic with Timedelta
# Used for finding "What is the date 7 days from now?"
today = date.today()
one_week_later = today + timedelta(days=7)
yesterday = today - timedelta(days=1)
print("Today:", today)
print("Next week:", one_week_later)
print("Yesterday:", yesterday)

# 4. Difference between two dates
d1 = date(2024, 1, 1)
d2 = date.today()
delta = d2 - d1
print(f"Days since start of year: {delta.days}")

# 5. Timestamp (Unix Time)
# Total seconds since Jan 1, 1970
ts = time.time()
print("Current Unix Timestamp:", ts)
print("Converted from TS:", datetime.fromtimestamp(ts))

# 6. Timezones (Advanced)
# Use zoneinfo (built-in in Python 3.9+)
from zoneinfo import ZoneInfo
utc_now = datetime.now(tz=ZoneInfo("UTC"))
est_now = datetime.now(tz=ZoneInfo("America/New_York"))
print("UTC:", utc_now)
print("EST:", est_now)

# Summary Table
"""
| Formatting | Meaning                            | Example        |
|------------|------------------------------------|----------------|
| %Y-%m-%d   | Year-Month-Day                     | 2024-12-25     |
| %I:%M %p   | Hour:Minute AM/PM                  | 03:30 PM       |
| %A         | Full Weekday name                  | Wednesday      |
| %B         | Full Month name                    | December       |
| timedelta  | Represent duration/time difference | days=1, hours=2|
"""
