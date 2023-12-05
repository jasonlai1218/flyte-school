from flytekit import task, workflow, ImageSpec, Resources

py_image_spec = ImageSpec(
    base_image="cr.flyte.org/flyteorg/flytekit:py3.9-1.8.1",
    env={"FLYTE_SDK_LOGGING_LEVEL": "20"},
    registry="harbor.linecorp.com/ecacda",
    platform="linux/amd64",
)
# py_image_spec = ImageSpec(
#     base_image="harbor.linecorp.com/ecacda/cr.flyte.org/flyteorg/flytekit:py3.9-1.8.1",
#     env={"Debug": "True"},
#     registry="harbor.linecorp.com/ecacda",
#     platform="linux/amd64",
# )
# py_image_spec = ImageSpec(
#     base_image="cr.flyte.org/flyteorg/flytekit:py3.9-1.8.1",
#     env={"Debug": "True"},
#     registry="cr.flyte.org/flyteorg",
#     platform="linux/amd64",
# )


@task(container_image=py_image_spec)
# @task
def t(a: int, b: int) -> int:
    return a + b


@workflow
def wf(a: int=5, b: int=3) -> int:
    out = t(a=a, b=b)
    return out


if __name__ == "__main__":
    # You can run workflows locally, it's just Python 🐍!
    print(f"{wf(a=10, b=10)}")
