import pytest
from sorts.merge_sort import merge_sort
from sorts.bubble import bubble_sort
from sorts.inserton import insertion_sort
from sorts.selection import selection_sort


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


def test_bubble_sort(array_1, array_2, array_3, array_4):

    assert sorted(array_1) == bubble_sort(array_1)
    assert sorted(array_2) == bubble_sort(array_2)

    assert sorted(array_3) == bubble_sort(array_3)
    assert sorted(array_4) == bubble_sort(array_4)


def test_insertion_sort(array_1, array_2, array_3, array_4):

    assert sorted(array_1) == insertion_sort(array_1)
    assert sorted(array_2) == insertion_sort(array_2)

    assert sorted(array_3) == insertion_sort(array_3)
    assert sorted(array_4) == insertion_sort(array_4)


def test_selection_sort(array_1, array_2, array_3, array_4):

    assert sorted(array_1) == selection_sort(array_1)
    assert sorted(array_2) == selection_sort(array_2)

    assert sorted(array_3) == selection_sort(array_3)
    assert sorted(array_4) == selection_sort(array_4)
