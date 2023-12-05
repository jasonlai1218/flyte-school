import datetime

from flytekit import task


@task(timeout=datetime.timedelta(hours=1))
def square(n: int) -> int:
    return n * n


print(square(n=10))
