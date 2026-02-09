import os
import sys
import datetime

print("=== Jenkins Freestyle Test ===")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Current time: {datetime.datetime.now()}")

# Simple test logic
a = 3
b = 7
print(f"3 + 7 = {a + b}")

print("Test completed successfully!")
