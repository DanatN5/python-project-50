import argparse

from gendiff.scripts.generate_diff import generate_diff



def main():
    description = 'Compares two configuration files and shows a difference.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        metavar='FORMAT',
                        help='set format out of output (default: stylish)')

    args = parser.parse_args()
    
    return generate_diff(args.first_file, args.second_file, format_name=args.format)




if __name__ == "__main__":
    main()