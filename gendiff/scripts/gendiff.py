import argparse

parser = argparse.ArgumentParser(description="""
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit""")

def main():
    print('Yo!')
    


if __name__ == "__main__":
    main()