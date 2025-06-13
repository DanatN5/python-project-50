import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1, file2, format_name, expected',
    [
        ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'stylish', 'tests/test_data/expected_result_json.txt'),
        ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'plain', 'tests/test_data/expected_result_plain.txt'),
        ('tests/test_data/file1.yaml', 'tests/test_data/file2.yaml',
         'stylish', 'tests/test_data/expected_result_yaml.txt'),
        ('tests/test_data/file1.yaml', 'tests/test_data/file2.yaml',
         'plain', 'tests/test_data/expected_result_plain.txt'),
        ('tests/test_data/file1.json', 'tests/test_data/file2.json',
         'json', 'tests/test_data/expected_result_json_format.txt'),
        ('tests/test_data/file1.yaml', 'tests/test_data/file2.yaml',
         'json', 'tests/test_data/expected_result_json_format.txt'),
    ]
)
def test_generate_diff(file1, file2, format_name, expected):
    with open(expected) as file:
        expected_result = file.read()
    result = generate_diff(file1, file2, format_name=format_name)
    
    assert result.strip() == expected_result.strip()