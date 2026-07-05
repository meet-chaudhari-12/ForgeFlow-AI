from typing import List
from pydantic import BaseModel, Field


class ForgeFlowState(BaseModel):
    """
    Shared state shared between every ForgeFlow AI agent.
    """

    # User Input
    user_idea: str = ""

    # Planner Agent
    summary: str = ""
    requirements: List[str] = Field(default_factory=list)
    questions: List[str] = Field(default_factory=list)

    # Research Agent
    research_notes: List[str] = Field(default_factory=list)

    # Architect Agent
    architecture: str = ""

    # Coder Agent
    generated_code: str = ""

    # Reviewer Agent
    review_feedback: List[str] = Field(default_factory=list)

    # Documentation
    documentation: str = ""

    # Current Agent
    current_agent: str = ""