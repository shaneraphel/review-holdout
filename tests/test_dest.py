from review_holdout.review import review


def test_requires_paths():
    assert review([]) is None


def test_binds_paths():
    assert review(["ok"]) is True
