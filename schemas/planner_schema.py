from typing import List
from pydantic import BaseModel


class PlannerOutput(BaseModel):

    summary: str

    requirements: List[str]

    questions: List[str]