import argparse
from gendiff.load_files import load_files

def main():
    description = 'Compares two configuration files and shows a difference.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                         help='set format out of output')

    args = parser.parse_args()

    print(load_files(args.first_file, args.second_file))

    
    


if __name__ == "__main__":
    main()