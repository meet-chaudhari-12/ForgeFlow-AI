from tools.gemini import ask_gemini


def load_prompt():
    with open("prompts/architect.txt", "r", encoding="utf-8") as file:
        return file.read()


def architect_agent(summary, requirements, research_notes):

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

Project Summary:
{summary}

Requirements:
{chr(10).join("- " + r for r in requirements)}

Research Notes:
{chr(10).join("- " + r for r in research_notes)}
"""

    return ask_gemini(full_prompt)