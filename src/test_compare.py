from compare import compare_int, compare_lists

def test_compare_int():
    assert compare_int(0, 10) == 1
    assert compare_int(-31, 55) == -1
    assert compare_int(-24, -24) == 0

def test_compare_lists():
    assert compare_lists([], []) == 0
    assert compare_lists([-31, 55], [40]) == 1
    assert compare_lists([-24, -24], [-24, -32]) == -1
