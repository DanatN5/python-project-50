import json
from pathlib import Path

import yaml

from gendiff import generate_diff, parse_files

with open('tests/test_data/flat_diff.txt') as file:
    gendiff_result = file.read()


def test_gendiff_json():
    data1, data2 = parse_files('tests/test_data/file1.json',
                              'tests/test_data/file2.json')
     
    assert generate_diff(data1, data2) == gendiff_result


def test_gendiff_yaml():
    data1, data2 = parse_files('tests/test_data/file1.yaml',
                              'tests/test_data/file2.yml')
        
    assert generate_diff(data1, data2) == gendiff_result


def test_parse_files_json():
    path_json1 = 'tests/test_data/file1.json'
    path_json2 = 'tests/test_data/file2.json'
    with open(Path(path_json1)) as data1, open(Path(path_json2)) as data2:
        file1 = json.load(data1)
        file2 = json.load(data2)
     
    assert parse_files(path_json1, path_json2) == [file1, file2]


def test_parse_files_yaml():
    path_yaml1 = 'tests/test_data/file1.yaml'
    path_yaml2 = 'tests/test_data/file2.yml'
    with open(Path(path_yaml1)) as data1, open(Path(path_yaml2)) as data2:
        file1 = yaml.safe_load(data1)
        file2 = yaml.safe_load(data2)
     
    assert parse_files(path_yaml1, path_yaml2) == [file1, file2]