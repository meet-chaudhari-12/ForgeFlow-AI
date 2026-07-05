from tools.gemini import ask_gemini


def load_prompt():
    with open("prompts/researcher.txt", "r", encoding="utf-8") as file:
        return file.read()


def researcher_agent(summary: str, requirements: list):

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

Project Summary:
{summary}

Requirements:
{chr(10).join("- " + r for r in requirements)}
"""

    response = ask_gemini(full_prompt)

    return response


def parse_research_output(text: str):

    notes = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("-"):
            notes.append(line[1:].strip())

    return notes