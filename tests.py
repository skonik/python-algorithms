import pytest
from sorts.merge_sort import merge_sort


@pytest.fixture
def array_1():
    return [5, 4, 1, 8, 7, 2, 6, 3]


@pytest.fixture
def array_2():
    return [5, 4, 3]


@pytest.fixture
def array_3():
    return [5]


@pytest.fixture
def array_4():
    return []


def test_merge_sort(array_1, array_2, array_3, array_4):

    assert sorted(array_1) == merge_sort(array_1)
    assert sorted(array_2) == merge_sort(array_2)

    assert sorted(array_3) == merge_sort(array_3)
    assert sorted(array_4) == merge_sort(array_4)
