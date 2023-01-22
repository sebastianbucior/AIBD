import pytest
from app import bubble_sort


testdata_1 = [
    ([6,0,8,3,1,2,7,9,4,5], [0,1,2,3,4,5,6,7,8,9]),
    ([2,2,2,2,2,2], [2,2,2,2,2,2])
    ]

@pytest.mark.parametrize('input, expected_output', testdata_1)
def test_sort(input, expected_output):
    assert bubble_sort(input) == expected_output

testdata_2 = [
    ('data', None),
    ([2,2,2,2,'s',2], None)
    ]
@pytest.mark.parametrize('input, expected_output', testdata_2)
def test_sort_input(input, expected_output):
    assert bubble_sort(input) == expected_output


testdata_3 = [
    ([0,1,2,3,4,5], 1),
    ([5,0,1,2,3,4], 2),
    ([5,4,0,1,2,3], 3)
    ]
@pytest.mark.parametrize('input, expected_output', testdata_3)
def test_sort_ite(input, expected_output):
    assert bubble_sort(input, True)[1] == expected_output