from review_holdout.suite import verdict


def test_missing_tests_unscored():
    assert verdict([], lambda p: True) is None


def test_failures_count():
    assert verdict(["a"], lambda p: False) is False
    assert verdict(["a"], lambda p: True) is True
