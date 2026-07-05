import os


def save_report(state):

    os.makedirs("reports", exist_ok=True)

    filename = state.user_idea.lower().replace(" ", "_") + "_report.md"

    path = os.path.join("reports", filename)

    with open(path, "w", encoding="utf-8") as file:

        file.write("# ForgeFlow AI Report\n\n")

        file.write("## User Idea\n")
        file.write(state.user_idea + "\n\n")

        file.write("## Summary\n")
        file.write(state.summary + "\n\n")

        file.write("## Requirements\n")

        for item in state.requirements:
            file.write(f"- {item}\n")

        file.write("\n## Questions\n")

        for item in state.questions:
            file.write(f"- {item}\n")

        file.write("\n## Research Notes\n")

        for item in state.research_notes:
            file.write(f"- {item}\n")

        file.write("\n## Architecture\n")
        file.write(state.architecture + "\n\n")

        file.write("\n## Implementation Plan\n")
        file.write(state.generated_code + "\n\n")

        file.write("\n## Review\n")

        for item in state.review_feedback:
            file.write(f"- {item}\n")

        file.write("\n## Documentation\n")
        file.write(state.documentation)

    return path