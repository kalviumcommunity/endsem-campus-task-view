def select_tasks(tasks, mode):
    # Supported modes: all, unfinished.
    return list(tasks)


def titles_for_view(tasks, mode="all"):
    selected = select_tasks(tasks, mode)
    return [task["title"] for task in selected]
