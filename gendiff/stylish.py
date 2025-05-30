import itertools

def stringify(data, replacer='.', count=4):
    
    def walk(item, depth):
        if not isinstance(item, dict):
            return str(item)
        
        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        keys = item.keys()
        strings = list(map(
        lambda key:
        f'{deep_indent}{str(key)}: {walk(item[key], deep_indent_size)}',
        keys))
            
        result = itertools.chain('{', strings, [current_indent + '}'])
        return '\n'.join(result)
    return walk(data, 0)

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

a, b = parse_files('tests/test_data/file3.json', 'tests/test_data/file4.json')

def generate_diff(data1, data2):
    common_keys = sorted(data1.keys() | data2. keys())
    result = {}        
    for key in common_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)
        if key not in data1:
            result[key] = {'status':'added',
                           'value': val2}
        elif key not in data2:
            result[key] = {'status':'deleted',
                           'value': val1}
        elif isinstance(val1, dict) and isinstance(val2, dict):
            result[key] = {'status': 'nested',
                           'children': generate_diff(val1, val2)}
        elif val2 != val1:
            result[key] = {'status':'updated',
                           'old_value': val1,
                           'new_value': val2}
        else:
            result[key] = {'status':'unchanged',
                           'value': val1}
    return result

print(stringify(generate_diff(a, b)))