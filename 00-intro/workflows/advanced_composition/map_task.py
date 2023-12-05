from typing import List

from flytekit import task, workflow, map_task, Resources

# Doc:https://docs.flyte.org/projects/cookbook/en/latest/auto_examples/advanced_composition/map_task.html#map-task

@task
def a_mappable_task(a: int) -> str:
    inc = a + 2
    stringified = str(inc)
    return stringified


@task
def coalesce(b: List[str]) -> str:
    coalesced = "".join(b)
    return coalesced


@workflow
def my_map_workflow(a: List[int]) -> str:
    mapped_out = map_task(a_mappable_task)(a=a).with_overrides(
        requests=Resources(mem="300Mi"),
        limits=Resources(mem="500Mi"),
        retries=1,
    )
    coalesced = coalesce(b=mapped_out)
    return coalesced


if __name__ == "__main__":
    result = my_map_workflow(a=[1, 2, 3, 4, 5])
    print(f"{result}")
