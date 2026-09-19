"""Open leftover dest: empty test lists are unscored."""

def _passed(path):
    return path != "fail"

def review(test_paths):
    n_failed = sum(1 for path in test_paths if not _passed(path))
    if not test_paths:
        return None
    return n_failed == 0
