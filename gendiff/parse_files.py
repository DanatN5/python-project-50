import json
from pathlib import Path

import yaml


def parse_files(file1_name1, file_name2):
    
    with open(Path(file1_name1)) as data1, open(Path(file_name2)) as data2:
        if Path(file1_name1).suffix == '.json':
            file1 = json.load(data1)
            file2 = json.load(data2)

        elif Path(file1_name1).suffix == '.yaml' or '.yml':
            file1 = yaml.safe_load(data1)
            file2 = yaml.safe_load(data2)
    
    return [file1, file2]


print(parse_files('tests/test_data/file1.yaml', 'tests/test_data/file2.yml'))