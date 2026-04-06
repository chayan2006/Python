# 📝 Logging: Tracking Your Program's Progress

import logging

# 1. Basic Configuration
# We specify where to save logs (filename), what format, and level
logging.basicConfig(
    filename="app_logs.log",
    level=logging.DEBUG, # Log EVERYTHING higher than or equal to DEBUG
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# 2. Logging Levels (Ordered by importance)
logging.debug("Lowest priority: Use this for diagnostics and finding bugs")
logging.info("Information: Used for important program flow steps")
logging.warning("Warning: Something unexpected but program still works")
logging.error("Error: A function failed completely (Exception happened)")
logging.critical("Critical: The whole application might crash!")

# 3. Logging into a file and the console (Advanced)
# If you want to see logs in BOTH the console and a file:
logger = logging.getLogger("MyLogger") 
# Add handlers for both file and console if needed...

# 4. Use Case: Logging Exceptions
# This is much better than just using print()
try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error("Division by zero occurred!", exc_info=True) # Full stack trace!

print("Logged the error in app_logs.log. Check it out!")

# Summary of Log Levels
"""
| Level     | Numeric | Meaning (When to use?)                           |
|-----------|---------|--------------------------------------------------|
| DEBUG     | 10      | Information for programmers (highly detailed)   |
| INFO      | 20      | Program flow (e.g. Server started on port 5001) |
| WARNING   | 30      | Program will continue, but check this!          |
| ERROR     | 40      | Exception occurred (e.g. File not found)         |
| CRITICAL  | 50      | The app cannot continue (e.g. Database is down)  |
"""
