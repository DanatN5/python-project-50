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
    keys = sorted(data1.keys() | data2. keys())
    result = '{\n'
    for key in keys:
        if key not in data1:
            result += f'  + {str(key)}: {str(data2[key])}\n'
        elif key not in data2:
            result += f'  - {str(key)}: {str(data1[key])}\n'
        elif data1[key] == data2[key]:
            result += f'    {str(key)}: {str(data1[key])}\n'
        else:
            result += (
                f'  - {str(key)}: {str(data1[key])}\n'
                f'  + {str(key)}: {str(data2[key])}\n'
            )
    result += '}'
    
    return result


if __name__ == "__main__":
    main()