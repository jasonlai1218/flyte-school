import typing
from datetime import timedelta

from flytekit import wait_for_input, task, workflow

# Doc:https://docs.flyte.org/projects/cookbook/en/latest/auto_examples/advanced_composition/waiting_for_external_inputs.html


@task
def create_report(data: typing.List[float]) -> dict:  # o0
    """A toy report task."""
    return {
        "mean": sum(data) / len(data),
        "length": len(data),
        "max": max(data),
        "min": min(data),
    }


@task
def finalize_report(report: dict, title: str) -> dict:
    return {"title": title, **report}


@workflow
def reporting_wf(data: typing.List[float]) -> dict:
    report = create_report(data=data)
    title_input = wait_for_input("title", timeout=timedelta(hours=1), expected_type=str)
    return finalize_report(report=report, title=title_input)


if __name__ == "__main__":
    print(reporting_wf(data=[1.0, 2.0, 3.0, 4.0, 5.0]))
