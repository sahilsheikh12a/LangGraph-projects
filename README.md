# LangGraph Practice Projects

This repository contains my hands-on LangGraph and LangChain practice work, including a small Streamlit chatbot app and multiple Jupyter notebooks that explore different workflow patterns.

## Project Structure

- `app/frontend.py`: Streamlit chat interface with per-session thread IDs and chat history.
- `app/langgraph_backend.py`: LangGraph-based chatbot backend using `StateGraph`, `InMemorySaver`, and OpenAI chat models.
- `scripts/api_smoke_test.py`: Small API connectivity test for the OpenAI-backed model.
- `notebooks/`: notebook experiments covering installation, chatbot setup, prompt chaining, LLM workflows, parallel workflows, BMI workflow logic, and an X post generator.

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

You can also copy the sample file:

```bash
cp .env.example .env
```

## Run The Chatbot

```bash
streamlit run app/frontend.py
```

## Optional API Smoke Test

```bash
python scripts/api_smoke_test.py
```

## Notes

- The local virtual environment and secrets are excluded from Git.
- This repo is mainly a learning and experimentation workspace for LangGraph concepts and small AI workflow prototypes.
