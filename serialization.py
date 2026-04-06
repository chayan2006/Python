# 📦 Serialization: Saving Complex Objects to Files

import pickle
import shelve

# 1. Pickle: Saving a single data structure (List, Dict, or Object)
# Think of this as "Freezing" a Python object to disk
data = {"users": ["Chayan", "Deepmind"], "score": 100}

# Writing to a binary file (.pkl)
with open("game_save.pkl", "wb") as f:
    pickle.dump(data, f)

# Reading from a binary file
with open("game_save.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    print("Loaded Data:", loaded_data)

# 2. Shelve: Persistent Dictionary (Like a small Database)
# Use this when you want to save MULTIPLE keys and values to a file
# and access them like a real Python dictionary!
with shelve.open("user_settings") as settings:
    settings["theme"] = "dark"
    settings["font_size"] = 16
    settings["language"] = "python"
    
    # Check if a key exists
    if "theme" in settings:
        print("User Preferred Theme:", settings["theme"])

# 3. Serialization Safety (JSON vs Pickle)
# JSON: Best for strings/numbers/lists across languages
# Pickle: Best for complex Python objects (Classes)
# CAUTION: NEVER unpickle data from untrusted sources (It can execute code!)

# Summary Table
"""
| Tool        | Best Case                                         | Pros / Cons                 |
|-------------|---------------------------------------------------|-----------------------------|
| json        | Web APIs, Simple data types                       | Text-based, Cross-language  |
| pickle      | Python-specific complex objects (e.g. Models)     | Binary, Python-only          |
| shelve      | Persistent storage of multiple variables           | Works like a dictionary     |
| csv         | Tabular data (Excel-like)                         | Human readable, No nesting  |
| sqlite3     | Large datasets with complex queries               | Real database, Scalable      |
"""
