# 🕵️ Regular Expressions (Regex) in Python

import re

# 1. Why use Regex?
# To find, extract, or replace text patterns like Emails, Phone Numbers, or URLs.

# 🚀 Basic Methods:
# re.search(): Find the FIRST occurrence
# re.findall(): Find ALL occurrences (Returns a list)
# re.split(): Split string based on pattern
# re.sub(): Substitute (Replace) pattern matches

# 2. Key Characters (Common Patterns)
# ^: Starts with
# $: Ends with
# .: Any character (except newline)
# \d: Any Digit (0-9)
# \w: Any Word Character (a-z, A-Z, 0-9, _)
# \s: Any Whitespace (Space, Tab, etc.)
# *: Zero or more (greedy)
# ?: Zero or one (optional)
# +: One or more

# 3. Practice Case: Email Extraction
text = "Contact us at support@example.com or admin_user@my.org for help."
email_pattern = r"[\w\.-]+@[\w\.-]+" # Simple email pattern
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# 4. Search and Replace
text = "The price is $100 for the item."
# Replace digits with 'X'
censored = re.sub(r"\d+", "X", text)
print("Censored:", censored)

# 5. Compilation for Performance
# (If you're using the same pattern many times)
email_regex = re.compile(email_pattern)
result = email_regex.search("my_email@abc.com")
if result:
    print("Email pattern matched successfully!")

# Summary Table
"""
| Pattern | Meaning                             | Example (Match)     |
|---------|-------------------------------------|---------------------|
| [a-z]   | Any lowercase letter                | 'h', 'e', 'l', 'o' |
| [0-9]   | Any single digit                    | '5', '8'            |
| \d{3}   | Exactly 3 digits                    | '123'               |
| \w+     | One or more word characters         | 'hello_123'         |
| ^Hello  | Starts with Hello                   | 'Hello world'       |
| bye$    | Ends with bye                       | 'The end, bye'      |
"""
