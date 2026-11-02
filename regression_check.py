from copy import deepcopy
from sample_data import TASKS
from task_view import titles_for_view


def check(label, actual, expected):
    assert actual == expected, f"{label}: actual={actual!r}, expected={expected!r}"
    print(f"PASS {label}: {actual!r}")


def run_checks():
    before = deepcopy(TASKS)
    expected_default = None  # COMPLETE from requirements and sample_data.py
    expected_unfinished = None  # COMPLETE from requirements and sample_data.py
    check("mixed default", titles_for_view(TASKS), expected_default)
    check("mixed unfinished", titles_for_view(TASKS, "unfinished"), expected_unfinished)
    check("mixed all", titles_for_view(TASKS, "all"), ["Book room", "Print posters", "Check microphones"])
    completed = [{"title": "Done", "completed": True, "priority": "high"}]
    check("completed-only default", titles_for_view(completed), [])
    check("completed-only unfinished", titles_for_view(completed, "unfinished"), [])
    low = [{"title": "Low unfinished", "completed": False, "priority": "low"}]
    check("low priority unfinished", titles_for_view(low), ["Low unfinished"])
    for mode in (None, "unfinished", "all"):
        actual = titles_for_view([]) if mode is None else titles_for_view([], mode)
        check(f"empty {mode}", actual, [])
    check("mixed records and order preserved", TASKS, before)
    check("completed input preserved", completed, [{"title": "Done", "completed": True, "priority": "high"}])
    check("low input preserved", low, [{"title": "Low unfinished", "completed": False, "priority": "low"}])
    print("Complete regression passed")


if __name__ == "__main__":
    run_checks()
