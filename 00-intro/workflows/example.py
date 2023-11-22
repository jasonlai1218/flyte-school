from flytekit import task, workflow


@task
def t(a: int, b: int) -> int:
    return a + b


@workflow
def wf(a: int=5, b: int=3) -> int:
    out = t(a=a, b=b)
    return out


if __name__ == "__main__":
    # You can run workflows locally, it's just Python 🐍!
    print(f"{wf(a=10, b=10)}")
