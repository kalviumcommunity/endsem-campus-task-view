from sample_data import TASKS
from task_view import titles_for_view

print("Input:", TASKS)
print("Default:", titles_for_view(TASKS))
print("All:", titles_for_view(TASKS, "all"))
