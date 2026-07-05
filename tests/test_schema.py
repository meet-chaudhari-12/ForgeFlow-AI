from schemas.planner_schema import PlannerOutput

output = PlannerOutput(
    summary="Weather Dashboard",
    requirements=[
        "React Frontend",
        "FastAPI Backend"
    ],
    questions=[
        "Need Login?",
        "Need Forecast?"
    ]
)

print(output)