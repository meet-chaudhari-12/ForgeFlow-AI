import re

from tools.gemini import ask_gemini


def load_prompt():
    with open("prompts/planner.txt", "r", encoding="utf-8") as file:
        return file.read()


def planner_agent(user_idea: str):

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

User Idea:
{user_idea}
"""

    response = ask_gemini(full_prompt)

    return response


def parse_planner_output(text: str):

    summary = ""
    requirements = []
    questions = []

    lines = text.splitlines()

    mode = None

    for line in lines:

        line = line.strip()

        if line.startswith("Summary"):
            mode = "summary"
            continue

        if line.startswith("Requirements"):
            mode = "requirements"
            continue

        if line.startswith("Questions"):
            mode = "questions"
            continue

        if mode == "summary":
            if line:
                summary += line + " "

        elif mode == "requirements":
            if line.startswith("-"):
                requirements.append(line[1:].strip())

        elif mode == "questions":
            if line.startswith("-"):
                questions.append(line[1:].strip())

    return summary.strip(), requirements, questions