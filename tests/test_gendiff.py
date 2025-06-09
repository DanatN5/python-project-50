import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1, file2, format_name, expected',
    [
        ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'stylish', 'tests/test_data/result_stylish.txt'),
        ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'plain', 'tests/test_data/result_plain.txt'),
        ('tests/test_data/file1.yml', 'tests/test_data/file2.yml',
         'stylish', 'tests/test_data/result_stylish.txt'),
        ('tests/test_data/file1.yml', 'tests/test_data/file2.yml',
         'plain', 'tests/test_data/result_plain.txt'),
    ]
)
def test_generate_diff(file1, file2, format_name, expected):
    with open(expected) as file:
        expected_result = file.read()
    result = generate_diff(file1, file2, format_name=format_name)
    
    assert result == expected_result