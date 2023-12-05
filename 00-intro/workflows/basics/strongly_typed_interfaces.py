from flytekit import task, workflow

# Doc:https://docs.flyte.org/projects/cookbook/en/latest/getting_started/tasks_and_workflows.html#tasks-are-strongly-typed

# @task
# def square(x: float) -> float:
#     return x ** 2


@task
def square(x: str) -> float:
    return x ** 2


square(x=10.0)
# @workflow
# def wf() -> float:
#     return square(x=10.0)
