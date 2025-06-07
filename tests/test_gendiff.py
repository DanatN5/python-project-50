import json
from pathlib import Path

import pytest
import yaml

from gendiff import generate_diff, parse_files


@pytest.mark.parametrize(
    'file1, file2, format_name, expected',
    [
        ('tests/test_data/file11.json', 'tests/test_data/file21.json',
         'stylish', 'tests/test_data/result_stylish.txt'),
         ('tests/test_data/file11.json', 'tests/test_data/file21.json',
         'plain', 'tests/test_data/result_plain.txt'),
         ('tests/test_data/file11.yml', 'tests/test_data/file21.yml',
         'stylish', 'tests/test_data/result_stylish.txt'),
         ('tests/test_data/file11.yml', 'tests/test_data/file21.yml',
         'plain', 'tests/test_data/result_plain.txt'),
         ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'json', 'tests/test_data/json_diff.txt'),
         ('tests/test_data/file1.yaml', 'tests/test_data/file2.yaml',
         'json', 'tests/test_data/json_diff.txt'),
    ]
)
def test_generate_diff(file1, file2, format_name, expected):
    with open(expected) as file:
        expected_result = file.read()
    result = generate_diff(file1, file2, format_name=format_name)
    
    assert result == expected_result


def test_parse_files_json():
    path_json1 = 'tests/test_data/file1.json'
    path_json2 = 'tests/test_data/file2.json'
    with open(Path(path_json1)) as data1, open(Path(path_json2)) as data2:
        file1 = json.load(data1)
        file2 = json.load(data2)
     
    assert parse_files(path_json1, path_json2) == [file1, file2]


def test_parse_files_yaml():
    path_yaml1 = 'tests/test_data/file1.yaml'
    path_yaml2 = 'tests/test_data/file2.yaml'
    with open(Path(path_yaml1)) as data1, open(Path(path_yaml2)) as data2:
        file1 = yaml.safe_load(data1)
        file2 = yaml.safe_load(data2)
     
    assert parse_files(path_yaml1, path_yaml2) == [file1, file2]

