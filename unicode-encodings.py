# 📝 Mastering Unicode and Encodings: Text vs Binary Data

import sys

# 1. Why use Encodings? (Common Problem: "UnicodeEncodeError")
# Computers ONLY understand bits (0s and 1s). 
# We use Encodings (UTF-8, ASCII) to Map Letters to Bits!

# 🚀 Concept: String (Hello) -> Encoder (UTF-8) -> Bytes (Binary)

# 2. String to Bytes (Encoding)
text = "Hello, Python! 🐍"
# .encode() - String to Bytes
bytes_data = text.encode("utf-8")
print(f"Bytes: {bytes_data}") # Shown as b'...'

# 3. Bytes to String (Decoding)
decoded_text = bytes_data.decode("utf-8")
print(f"Decoded: {decoded_text}")

# 4. Common Encodings
# ASCII: 7-bit (Only basic English)
# UTF-8: 8-bit (The world standard - supports Emojis!)
# UTF-16: 16-bit (Mostly Windows/Java internal)

# 🚀 Troubleshooting Error: (Errors='replace' or 'ignore')
# Use this when you find a bad character in a file or network stream!
bad_bytes = b"\xff\xfe\x00" 
try:
    print(bad_bytes.decode("ascii"))
except UnicodeDecodeError:
    print("Replace bad byte with '?' instead of crashing!")
    print(bad_bytes.decode("ascii", errors="replace"))

# 5. Finding the System Default Encoding
print("System Default Encoding:", sys.getdefaultencoding())

# Summary Table
"""
| Method         | From           | To             | Purpose                               |
|----------------|----------------|----------------|---------------------------------------|
| .encode()      | str (Unicode)  | bytes (Binary) | Sending over network/saving to disk    |
| .decode()      | bytes (Binary) | str (Unicode)  | Reading from network/file buffer       |
| b"hello"       | Literal        | bytes          | Fast way to define binary data         |
| ord('A')       | Character      | Integer        | Find Unicode code point (65)           |
| chr(65)        | Integer        | Character      | Find character from code point ('A')   |
"""
