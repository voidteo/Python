#task 11: Print the current working directory using os.getcwd().
"""
import os
print(os.getcwd())

""" 
#task 12: Change the current working directory to a subfolder and verify with os.getcwd().
"""
import os

os.chdir()

"""
#task 35: Write “Hello, World!” to temp_data/greeting.txt using Path.write_text().

from pathlib import Path


Path.write_text(Path("./hi.txt"), "Hello")