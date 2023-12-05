from flytekit import LaunchPlan, current_context, task, workflow, CronSchedule


@task
def slope(x: list[int], y: list[int]) -> float:
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_x_squared = sum([x[i] ** 2 for i in range(len(x))])
    n = len(x)
    return (n * sum_xy - sum(x) * sum(y)) / (n * sum_x_squared - sum(x) ** 2)


@task
def intercept(x: list[int], y: list[int], slope: float) -> float:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    intercept = mean_y - slope * mean_x
    return intercept


@workflow
def simple_wf(x: list[int], y: list[int]) -> float:
    slope_value = slope(x=x, y=y)
    intercept_value = intercept(x=x, y=y, slope=slope_value)
    return intercept_value

# default_lp = LaunchPlan.get_default_launch_plan(current_context(), simple_wf)
# default_lp(x=[-3, 0, 3], y=[7, 4, -2])


# simple_wf_lp = LaunchPlan.create(
#     name="simple_wf_lp", workflow=simple_wf, default_inputs={"x": [-3, 0, 3], "y": [7, 4, -2]}
# )
# simple_wf_lp()
cron_lp = LaunchPlan.get_or_create(
    name="simple_lp",
    workflow=simple_wf,
    schedule=CronSchedule(
        schedule="0 1 * * *",
        kickoff_time_input_arg="kickoff_time",
    ),
)
