import argparse

from gendiff.parse_files import parse_files


def main():
    description = 'Compares two configuration files and shows a difference.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                         help='set format out of output')

    args = parser.parse_args()

    arg1, arg2 = parse_files(args.first_file, args.second_file)

    return generate_diff(arg1, arg2)


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



if __name__ == "__main__":
    main()