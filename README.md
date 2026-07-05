# 🚀 ForgeFlow AI

> Multi-Agent Software Engineering Platform powered by Google Gemini and LangGraph.

ForgeFlow AI is an AI-powered software engineering assistant that transforms a simple software idea into a complete project plan using multiple specialized AI agents.

Each AI agent has a dedicated responsibility such as planning, research, architecture design, implementation planning, review, and documentation generation.

---

# ✨ Features

- 🧠 Planner Agent (Atlas)
- 🔎 Research Agent (Scout)
- 🏗 Architect Agent (Forge)
- 💻 Coder Agent (Nova)
- 🛡 Reviewer Agent (Sentinel)
- 📝 Documentation Agent (Scribe)

---

# 🏗 Workflow

```text
User Idea
     │
     ▼
🧠 Atlas
     │
     ▼
🔎 Scout
     │
     ▼
🏗 Forge
     │
     ▼
💻 Nova
     │
     ▼
🛡 Sentinel
     │
     ▼
📝 Scribe
     │
     ▼
Final ForgeFlow Report
```

---

# 📂 Project Structure

```
ForgeFlow-AI
│
├── agents/
│
├── prompts/
│
├── graph/
│
├── reports/
│
├── utils/
│
├── tools/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Tech Stack

- Python
- LangGraph
- Google Gemini API
- Pydantic
- dotenv

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/meet-chaudhari-12/ForgeFlow-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the project

```bash
python main.py
```

---

# 📊 Output

ForgeFlow AI generates

- Project Summary
- Functional Requirements
- Clarification Questions
- Technology Research
- Software Architecture
- Implementation Plan
- Project Review
- Documentation
- Markdown Report

---

# 📈 Future Improvements

- JSON Output Parsing
- Tool Calling
- Memory Support
- Streamlit Web Interface
- PDF Report Export
- GitHub Repository Generation
- Multi-LLM Support
- Parallel Agent Execution

---

# 👨‍💻 Author

- Meet Chaudhari
- Vimal Solanki
- Aryan Vaghela

Built with ❤️ using LangGraph + Google Gemini.
