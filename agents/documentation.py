from tools.gemini import ask_gemini


def load_prompt():

    with open("prompts/documentation.txt", "r", encoding="utf-8") as file:
        return file.read()


def documentation_agent(summary, architecture):

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

Project Summary:
{summary}

Architecture:
{architecture}
"""

    return ask_gemini(full_prompt)