# LangGraph Practice Projects

This repository contains my hands-on LangGraph and LangChain practice work, including a small Streamlit chatbot app and multiple Jupyter notebooks that explore different workflow patterns.

## Included Work

- `frontend.py`: Streamlit chat interface with per-session thread IDs and chat history.
- `langgraph_backend.py`: LangGraph-based chatbot backend using `StateGraph`, `InMemorySaver`, and OpenAI chat models.
- `api_test.py`: Small API connectivity test for the OpenAI-backed model.
- `*.ipynb`: Notebook experiments covering installation, basic chatbot setup, prompt chaining, LLM workflows, parallel workflows, BMI workflow logic, and an X post generator.

## Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI via `langchain-openai`
- Streamlit
- Jupyter Notebook

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
pip install streamlit
```

3. Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run The Chatbot

```bash
streamlit run frontend.py
```

## Notes

- The local virtual environment and secrets are excluded from Git.
- This repo is mainly a learning and experimentation workspace for LangGraph concepts and small AI workflow prototypes.
