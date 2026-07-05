# 🚀 ForgeFlow AI - System Design

## Project Vision

ForgeFlow AI is an autonomous multi-agent software engineering platform that transforms a software idea into a structured development plan. Instead of relying on a single AI assistant, ForgeFlow AI simulates a collaborative software engineering team where specialized AI agents work together to analyze requirements, research technologies, design architecture, generate starter code, review implementations, and produce project documentation.

---

## Problem Statement

Most AI coding assistants simply generate code from a prompt. They rarely ask clarifying questions, plan the project, or follow a structured software development workflow.

ForgeFlow AI aims to solve this by introducing multiple AI agents that collaborate like a real software engineering team.

---

## Objectives

- Build a multi-agent software engineering platform.
- Demonstrate agent orchestration using LangGraph.
- Use Google Gemini as the reasoning engine.
- Maintain a shared state between agents.
- Produce structured outputs instead of plain text.
- Generate a complete project blueprint before implementation.

---

## Agent Workflow

User
↓
Planner Agent
↓
Research Agent
↓
Architect Agent
↓
Coding Agent
↓
Reviewer Agent
↓
Documentation Agent
↓
Final Output

---

## Agent Responsibilities

### Planner Agent
- Understand user requirements
- Ask clarifying questions
- Produce project requirements

### Research Agent
- Suggest technologies
- Recommend APIs
- Find best practices

### Architect Agent
- Design system architecture
- Suggest folder structure
- Create database design

### Coding Agent
- Generate starter implementation
- Generate important project files

### Reviewer Agent
- Review generated code
- Suggest improvements
- Identify missing components

### Documentation Agent
- Generate README
- Explain setup
- Produce project documentation

---

## Shared State

Each agent receives the current project state and updates it before passing it to the next agent.

The state contains:

- User Idea
- Requirements
- Research Notes
- Architecture
- Generated Code
- Review Feedback
- Documentation

---

## Tech Stack

- Python
- Google Gemini
- LangGraph
- Pydantic
- python-dotenv
- GitHub

---

## Future Scope

- Long-term memory
- MCP integration
- GitHub automation
- File generation
- Web interface