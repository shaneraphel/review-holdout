"""Suite verdict. Missing tests are not a pass."""

from __future__ import annotations

from collections.abc import Callable, Iterable


def verdict(test_paths: Iterable[str], _passed: Callable[[str], bool]) -> bool | None:
    test_paths = list(test_paths)
    n_failed = sum(1 for path in test_paths if not _passed(path))
    if not test_paths:
        return None
    return n_failed == 0
