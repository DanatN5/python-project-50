from gendiff.formatters import FORMATTERS
from gendiff.scripts.parse_files import parse_files


def generate_diff(data1, data2, format_name='stylish'):
        
    def diff(data1, data2):
        common_keys = sorted(data1.keys() | data2. keys())
        result = {}        
        for key in common_keys:
            val1 = data1.get(key)
            val2 = data2.get(key)
            if key not in data1:
                result[key] = {'status': 'added',
                               'value': val2}
            elif key not in data2:
                result[key] = {'status': 'deleted',
                               'value': val1}
            elif isinstance(val1, dict) and isinstance(val2, dict):
                result[key] = {'status': 'nested',
                               'children': diff(val1, val2)}
            elif val2 != val1:
                result[key] = {'status': 'updated',
                               'old_value': val1,
                               'new_value': val2}
            else:
                result[key] = {'status': 'unchanged',
                               'value': val1}
        return result

    arg1, arg2 = parse_files(data1, data2)
    difference = diff(arg1, arg2)    
    formatter = FORMATTERS.get(format_name)
    result = formatter(difference)
    return result