import json
from pathlib import Path

def load_files(file1, file2):
    
    with open(Path(file1)) as data1, open(Path(file2)) as data2:
        json_file1 = json.load(data1)
        json_file2 = json.load(data2)
    

    return [json_file1, json_file2]