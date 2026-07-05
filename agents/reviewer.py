from tools.gemini import ask_gemini


def load_prompt():
    with open("prompts/reviewer.txt", "r", encoding="utf-8") as file:
        return file.read()


def reviewer_agent(summary, architecture):

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

Project Summary:
{summary}

Architecture:
{architecture}
"""

    return ask_gemini(full_prompt)


def parse_review(text):

    feedback = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("-"):
            feedback.append(line[1:].strip())

    return feedback