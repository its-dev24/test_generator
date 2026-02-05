
# 🧪 Unit Test Generator

An automated tool designed to generate comprehensive unit tests for your code using Large Language Models (LLMs). This project bridges the gap between manual testing and automated code analysis, helping developers maintain high code coverage with minimal effort.

---

## 🚀 Overview

* **Purpose**: Automatically generate unit tests for provided source code.
* **Current Language Support**: Python.
* **AI Engine**: Powered by **OpenRouter** (Model: `llama-3.1-8b-instruct`).

## 🛠️ Tech Stack

* **Backend**: [FastAPI](https://fastapi.tiangolo.com/) - High-performance Python web framework.
* **Frontend**: [React](https://reactjs.org/) - Modern UI for seamless code input.
* **LLM API**: [OpenRouter](https://openrouter.ai/) - Unified interface for LLM access.

---

## 📂 Project Structure

```text
├── backend/        # FastAPI application and LLM logic
├── frontend/       # React application (UI)
├── .gitignore      # Git ignore rules
└── README.md       # Project documentation

```

---

## ⚙️ Getting Started

### 1. Prerequisites

* Python 3.8+
* Node.js & npm
* An [OpenRouter API Key](https://openrouter.ai/keys)

### 2. Backend Setup

Navigate to the backend directory and set up the environment:

```bash
# Go to backend
cd backend

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment Variables
# Create a .env file and add your key:
echo "OPENROUTER_API_KEY=your_api_key_here" > .env

# Run the server
uvicorn main:app --reload

```

### 3. Frontend Setup

Navigate to the frontend directory and launch the interface:

```bash
# Go to frontend
cd frontend

# Install dependencies
npm install

# Start the application
npm start

```

---

## 🗺️ Roadmap

### Phase 1: Frontend Revamp

* [ ] **Advanced Code Editor**: Integrate Monaco Editor (VS Code engine) for better syntax highlighting.
* [ ] **Real-time Streaming**: Implement Server-Sent Events (SSE) to stream test generation results.

### Phase 2: Structural Analysis

* [ ] **AST Parsing**: Use Python's `ast` module to analyze code structure, extract function signatures, and identify class dependencies before sending data to the LLM.
* [ ] **Code Contextualization**: Mapping local imports to provide the LLM with better context of the codebase.

### Phase 3: Multi-Agent System

* [ ] **Orchestration Layer**: Implementing a supervisor agent to manage specialized sub-agents.
* [ ] **Edge Case Agent**: Specialized in finding boundary conditions and "unhappy paths."
* [ ] **Security Agent**: Reviewing code for vulnerabilities and generating tests for exploit scenarios.
* [ ] **Refactoring Agent**: Providing code quality suggestions alongside the generated tests.

---

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Developed with ❤️ by [its-dev24*](https://github.com/its-dev24)


