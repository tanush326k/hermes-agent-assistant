# 🧠 Hermes Agent Assistant

A modular, lightweight AI agent system built with FastAPI that simulates advanced workflows: **Planner ➔ Executor ➔ Tools ➔ Memory**. It is designed to cleanly demonstrate how modern AI agents break down objectives, plan sequential actions, handle dynamic tool requests, and store context for future reasoning.

---

## 🚀 Quick Links

* **Live Demo:** [hermes-agent-tanush.onrender.com](https://hermes-agent-tanush.onrender.com)
* **GitHub Repository:** [github.com/tanush326k/hermes-agent-assistant](https://www.google.com/search?q=https://github.com/tanush326k/hermes-agent-assistant)

---

## ✨ Features

* **🧠 Task Planner:** A multi-step reasoning engine that slices abstract goals into structured action lists.
* **⚙️ Execution Engine:** A precise coordinator that runs the planned steps sequentially.
* **🔧 Tool-Based Architecture:** A decoupled layer for search, logic, and external utility integrations.
* **💾 Persistent Memory System:** Keeps execution contexts alive across sessions using localized tracking.
* **🌐 REST API (FastAPI):** High-performance backend endpoints providing lightning-fast interaction.
* **📄 Auto-Generated Docs:** Full OpenAPI specifications and Swagger playground natively accessible.

---

## 🏗️ Architecture Diagram

```text
        ┌──────────────┐
        │  User Input  │
        └──────┬───────┘
               │
               ▼
        ┌─────────────────┐
        │  FastAPI Layer  │
        └──────┬──────────┘
               │
               ▼
        ┌───────────────────┐
        │      Planner      │
        │  (Task Breakdown) │
        └──────┬────────────┘
               │
               ▼
        ┌───────────────────┐
        │     Executor      │
        │  (Step Execution) │
        └──────┬────────────┘
               │
               ▼
        ┌───────────────────┐
        │    Tools Layer    │
        │ (Utilities/Logic) │
        └──────┬────────────┘
               │
               ▼
        ┌───────────────────┐
        │   Memory System   │
        │ (Persistent Store)│
        └──────┬────────────┘
               │
               ▼
         Final Response

```

---

## 📡 API Endpoints

### 🟢 Root

* **Method:** `GET`
* **Path:** `/`
* **Purpose:** Verification heartbeat check.

### 🧠 Run Agent

* **Method:** `POST`
* **Path:** `/run`
* **Query Parameter:** `task=your task here`
* **Example Call:** `/run?task=analyze AI market trends`

### 📚 Interactive Docs

* **Path:** `/docs`
* **Purpose:** Fully active Swagger UI wrapper to test requests directly out of the browser.

---

## 🧠 How It Works

1. **Planner:** Takes raw incoming user requests and translates them into explicit steps.
2. **Executor:** Evaluates the steps one after the other in correct chronological order.
3. **Tools:** Act as functional extensions, handling specialized computations or lookups.
4. **Memory:** Encapsulates the results securely so successive logic runs can build off of them.

---

## ⚙️ Installation & Local Setup

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/tanush326k/hermes-agent-assistant.git
cd hermes-agent-assistant

# Initialize a clean virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 2. Dependency Management

```bash
# Install required production packages
pip install -r requirements.txt

```

### 3. Execution

```bash
# Run the local development server with live reload enabled
uvicorn app.main:app --reload

```

Once spun up, navigate your environment to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔮 Future Roadmap & Upgrades

* **LLM Integration:** Layering foundational model logic (Ollama, OpenAI, or Anthropic API hooks) directly over our routing.
* **Vector Memory Store:** Transitioning base serialization schemas over to semantic data retrieval (FAISS, ChromaDB).
* **Multi-Agent Coordination:** Orchestrating separate standalone workers interacting via a specialized internal communication mesh.
* **Tool Ecosystem Expansion:** Injecting robust functional engines including direct calculations, code runners, and web scraping utilities.

---

## 🔥 Pro Features (Optimization Submissions)

To take this framework to a production-grade enterprise setup, implement the following strategies:

* **⚡ Streaming Execution Mode:** Refactor the executor pipeline using Server-Sent Events (SSE) to emit real-time agent reasoning directly to client UIs.
* **🛠️ Deep Tool Expansion:** Provide native execution frameworks for an isolated `Calculator Tool`, a robust `Web Search API Tool`, and a local sandboxed `File Writer Tool`.
* **🗄️ Memory Upgrades:** Replace the JSON flatfile structure with a transactional local **SQLite database**, or migrate directly to an advanced **FAISS Vector Store** to handle complex context searches.
* **🤝 Multi-Agent Architecture:** Explode the core executor cycle into individual atomic agents:
* *Planner Agent:* Designs the master roadmap strategy.
* *Executor Agent:* Focused entirely on specialized tools calls.
* *Critic Agent:* Inspects outcomes and validates results against criteria.


* **💡 Explainable AI Mode:** Expose complete internal tracing structures inside your standard API response body, returning metadata for each planning pass and calculation adjustment.
