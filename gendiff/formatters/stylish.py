import itertools

def stylish_format(data, replacer='.', count=4):
    
    def walk(item, depth):
        def format_line(value, depth):
            current_indent = replacer * count * depth
            deep_indent = replacer * count * (depth+1)
            if isinstance(value, dict):
                lines = []
                for k, v in value.items():
                    lines.append(f"{deep_indent}{k}: {format_line(v, depth+1)}")
                result = itertools.chain('{', lines, [current_indent + '}'])
                return '\n'.join(result)        
            return str(value)
        
        deep_indent_size = depth * count - 2
        deep_indent = deep_indent_size * replacer
        current_indent = replacer * count * depth
        keys = sorted(item.keys())
        lines = []
        for key in keys:
            val = item[key]
            status = val['status']
            if status == 'added':             
                lines.append(f'{deep_indent}+ {str(key)}: {format_line(val['value'], depth+1)}')
            elif status == 'deleted':
                lines.append(f'{deep_indent}- {str(key)}: {format_line(val['value'], depth+1)}')
            elif status == 'unchanged':
                lines.append(f'{deep_indent}  {str(key)}: {format_line(val['value'], depth+1)}')
            elif status == 'updated':
                lines.append(f'{deep_indent}- {str(key)}: {format_line(val['old_value'], depth+1)}\n'
                             f'{deep_indent}+ {str(key)}: {format_line(val['new_value'], depth+1)}')
            elif status == 'nested':
                lines.append(f"{deep_indent}  {str(key)}: {walk(val['children'], depth+1)}")
            
        result = itertools.chain('{', lines, [current_indent + '}'])
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

print(stylish_format(generate_diff(a, b)))
