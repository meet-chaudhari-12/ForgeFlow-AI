import time

from graph.state import ForgeFlowState
from graph.workflow import workflow
from utils.report_writer import save_report


def print_section(title):
    print("\n" + "─" * 45)
    print(title)
    print("─" * 45)


def print_list(items):
    if not items:
        print("None")
        return

    for item in items:
        print(f"• {item}")


def main():

    print("\n🚀 ForgeFlow AI")
    print("🤖 Multi-Agent Software Engineer")
    print("────────────────────────────────────")

    idea = input("\nEnter your software idea:\n> ")

    state = ForgeFlowState(user_idea=idea)

    start_time = time.time()

    result = workflow.invoke(state)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\n")
    print("=" * 45)
    print("🚀 FINAL FORGEFLOW REPORT")
    print("=" * 45)

    print_section("📌 User Idea")
    print(result["user_idea"])

    print_section("📄 Summary")
    print(result["summary"])

    print_section("📋 Requirements")
    print_list(result["requirements"])

    print_section("❓ Questions")
    print_list(result["questions"])

    print_section("🔎 Research Notes")
    print_list(result["research_notes"])

    print_section("🏗 Architecture")
    print(result["architecture"])

    print_section("💻 Implementation Plan")
    print(result["generated_code"])

    print_section("🔰 Review")
    print_list(result["review_feedback"])

    print_section("📝 Documentation")
    print(result["documentation"])

    # Convert LangGraph result back into ForgeFlowState
    final_state = ForgeFlowState(**result)

    report_path = save_report(final_state)

    print("\n📁 Report saved successfully!")
    print(report_path)

    print(f"\n⚡ Total Execution Time : {execution_time:.2f} seconds")

    print("\n" + "=" * 45)
    print("🎉 ForgeFlow AI Completed Successfully!")
    print("=" * 45)

    print("\nExecuted Agents")
    print("✅ 🧠 Atlas      (Planner)")
    print("✅ 🔎 Scout      (Researcher)")
    print("✅ 🏗 Forge      (Architect)")
    print("✅ 💻 Nova       (Coder)")
    print("✅ 🔰 Sentinel   (Reviewer)")
    print("✅ 📝 Scribe     (Documentation)")

    print("\n📄 Final report generated successfully!")
    print("🚀 Thank you for using ForgeFlow AI!")


if __name__ == "__main__":
    main()