from flytekit import task


@task
def square(x: float) -> float:
    return x ** 2


print(square(x=2.0))

