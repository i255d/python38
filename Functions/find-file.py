#!/usr/bin/python3


import os
file_name = "get-wmi.py"
start_path = "C:\vsts\IA\python38\"

# def find(file_name, start_path):
#     for root, dirs, files in os.walk(start_path):
#         # if file_name in files:
#         if file_name in file or file_name in dirs:
#             return os.path.join(root, file_name)
from pathlib import Path
p = Path(start_path)
for name in p.glob('*.p*'):
    print(name)


