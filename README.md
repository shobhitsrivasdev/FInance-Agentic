# Financial Agent

An AI-powered financial research assistant that can analyze market data, generate financial reports, and interact with you through text or voice.

## Features

- **Financial Data Analysis**  
  Fetches and analyzes financial information like stock performance, company news, and market trends.

- **Automatic Financial Reports**  
  Generates clear, professional reports summarizing financial data.

- **Interactive Chat**  
  Ask questions about finance and get AI-powered answers.

- **Voice Support**  
  Speak to the agent and receive spoken responses.

## Requirements

- Python 3.10+
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shobhitsrivasdev/FInance-Agentic
   cd financial_agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your environment variables**
   ```bash
   export OPENAI_API_KEY="your_api_key"      # Mac/Linux
   set OPENAI_API_KEY="your_api_key"         # Windows
   ```

## Usage

### Text Mode
Run the financial agent in text mode:
```bash
python -m financial_research_agent.main
```

### Voice Mode
Run the financial agent in voice mode:
```bash
python -m financial_research_agent.mainvoice
```

## How It Works

1. **User Input** – You type or speak your question.
2. **AI Processing** – The OpenAI Agent fetches and analyzes financial data.
3. **Report Generation** – The system creates a financial report or answers your question.
4. **Output** – You receive the result in text or voice.

```
[User] --> [Agent] --> [Data Fetch + Analysis] --> [AI Report] --> [Text/Voice Response]
```
