from flytekit import task


@task
def hello():
    print("hello world")


hello()
