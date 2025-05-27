from gendiff import generate_diff, load_files


def test_gendiff():
    data1, data2 = load_files('tests/test_data/file1.json',
                              'tests/test_data/file2.json')
    with open('tests/test_data/flat_diff.txt') as file:
        result = file.read()
    
    assert generate_diff(data1, data2) == result
    

test_gendiff()

