import json
from collections import defaultdict
import sys

# file_path = input("Enter path to JSON file or file name:")

if len(sys.stdin) > 1:
    print("Please pass in one file as a time.")
else: 
    for line in sys.stdin:
        with open(line, "r") as dag_file: 
            dag_dict = json.loads(dag_file.read())


