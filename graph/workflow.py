from langgraph.graph import StateGraph, START, END

from graph.state import ForgeFlowState

from agents.planner import (
    planner_agent,
    parse_planner_output
)

from agents.researcher import (
    researcher_agent,
    parse_research_output
)

from agents.architect import architect_agent

from agents.coder import coder_agent

from agents.reviewer import (
    reviewer_agent,
    parse_review
)

from agents.documentation import documentation_agent


def planner_node(state: ForgeFlowState):

    print("\n🧠 Atlas is thinking...\n")

    response = planner_agent(state.user_idea)

    summary, requirements, questions = parse_planner_output(response)

    state.summary = summary
    state.requirements = requirements
    state.questions = questions
    state.current_agent = "Planner"

    print("✅ Planning Complete")

    return state


def researcher_node(state: ForgeFlowState):

    print("\n🔎 Scout is researching...\n")

    response = researcher_agent(
        state.summary,
        state.requirements
    )

    notes = parse_research_output(response)

    state.research_notes = notes
    state.current_agent = "Researcher"

    print("✅ Research Complete")

    return state


def architect_node(state: ForgeFlowState):

    print("\n🏗 Forge is designing architecture...\n")

    response = architect_agent(
        state.summary,
        state.requirements,
        state.research_notes
    )

    state.architecture = response
    state.current_agent = "Architect"

    print("✅ Architecture Complete")

    return state


def coder_node(state: ForgeFlowState):

    print("\n💻 Nova is creating implementation plan...\n")

    response = coder_agent(
        state.architecture
    )

    state.generated_code = response
    state.current_agent = "Coder"

    print("✅ Implementation Plan Ready")

    return state


def reviewer_node(state: ForgeFlowState):

    print("\n🔰 Sentinel is reviewing...\n")

    response = reviewer_agent(
        state.summary,
        state.architecture
    )

    state.review_feedback = parse_review(response)
    state.current_agent = "Reviewer"

    print("✅ Review Complete")

    return state


def documentation_node(state: ForgeFlowState):

    print("\n📝 Scribe is writing documentation...\n")

    response = documentation_agent(
        state.summary,
        state.architecture
    )

    state.documentation = response
    state.current_agent = "Documentation"

    print("✅ Documentation Generated")

    return state


builder = StateGraph(ForgeFlowState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("architect", architect_node)
builder.add_node("coder", coder_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("documentation", documentation_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "architect")
builder.add_edge("architect", "coder")
builder.add_edge("coder", "reviewer")
builder.add_edge("reviewer", "documentation")
builder.add_edge("documentation", END)

workflow = builder.compile()