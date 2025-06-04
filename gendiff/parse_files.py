import json
from pathlib import Path

import yaml


def parse_files(file1_name1, file_name2):
    
    suffix = Path(file1_name1).suffix
    with open(Path(file1_name1)) as data1, open(Path(file_name2)) as data2:
        if suffix == '.json':
            file1 = json.load(data1)
            file2 = json.load(data2)

        elif suffix == '.yaml' or suffix == '.yml':
            file1 = yaml.safe_load(data1)
            file2 = yaml.safe_load(data2)
    
    return [file1, file2]
