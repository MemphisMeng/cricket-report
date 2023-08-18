import functions
from functions import *

def test_extract_raw_data(mocker):
    mock_urlopen = mocker.patch("functions.urlopen", return_value=open('tests_female_json.zip', 'rb'))

    actual_result = extract_raw_data('www.dummy.com')
    assert mock_urlopen.call_count == 1 # numbers of urlopen being called
    assert len(actual_result) == 2 # a tuple of matches and innings


# def calculate(x, y):
#     return x + y

# def func(x, y):
#     return calculate(x, y) + calculate(y, x)

# def test_func(mocker):
#     mock_calculate = mocker.patch("calculate", return_value=4)
#     actual_result = func(4, 4)
#     assert mock_calculate.call_count == 2
