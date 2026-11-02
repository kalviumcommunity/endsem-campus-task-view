from copy import deepcopy
from sample_data import TASKS
from task_view import titles_for_view

before = deepcopy(TASKS)
assert titles_for_view(TASKS, "all") == ["Book room", "Print posters", "Check microphones"]
assert titles_for_view([], "all") == []
assert TASKS == before
print("Existing checks passed: explicit all, empty all, input unchanged")
