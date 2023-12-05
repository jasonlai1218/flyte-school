from flytekit import task

# Doc:https://docs.flyte.org/projects/cookbook/en/latest/auto_examples/development_lifecycle/task_cache.html


@task(cache=True, cache_version="1.0")  # noqa: F841
def square(n: int) -> int:
    """
     Parameters:
        n (int): name of the parameter for the task will be derived from the name of the input variable.
                 The type will be automatically deduced to ``Types.Integer``.

    Return:
        int: The label for the output will be automatically assigned, and the type will be deduced from the annotation.

    """
    return n * n


print(square(n=10))
