# 🛡️ ThreatShield AI
### Autonomous AI-Powered Network Threat Detection & Response Agent

[![Google ADK](https://img.shields.io/badge/Framework-Google%20ADK-blue)](https://github.com/google/agents-core)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Gemini](https://img.shields.io/badge/Model-Gemini%201.5%20Pro-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

ThreatShield AI is an autonomous cybersecurity agent developed for the **Google Kaggle AI Agents: Intensive Vibe Coding Capstone Project** using **Google ADK**, **Gemini 1.5 Pro**, and **Antigravity IDE**.

The system analyzes network security logs, identifies suspicious activities, recommends or performs automated responses, and protects itself against prompt injection attacks through built-in safety guardrails.

The objective is to demonstrate how modern AI agents can assist Security Operations Centers (SOC) by reducing manual investigation time and improving incident response.

---

# ✨ Key Features

- 🔍 AI-powered network log analysis
- 🚨 Real-time threat detection
- 🔥 Automated firewall blocking
- 👨‍💻 Human escalation for critical incidents
- 🧠 Multi-turn conversation memory
- 🛡️ Prompt Injection Protection
- 📊 Interactive Streamlit Dashboard
- ⚡ Built using Google ADK Agent Framework

---

# 📸 Project Demo

## Security Operations Dashboard

<img width="1460" height="829" alt="Image" src="https://github.com/user-attachments/assets/8bc5e457-e43f-476b-8517-3ad4ce608569" />

---

## Prompt Injection Guardrails

<img width="1459" height="736" alt="Image" src="https://github.com/user-attachments/assets/471ae193-e795-4fbc-82f0-fd9c3f8e1473" />

---

# 🏗️ Architecture

```
                    Network Logs
                          │
                          ▼
                Data Ingestion Layer
                          │
                          ▼
                Gemini 1.5 Pro Agent
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
 Threat Detection                  Safety Guardrails
          │                               │
          └───────────────┬───────────────┘
                          ▼
                Decision & Reasoning
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
 Firewall Block                  Human Escalation
                          │
                          ▼
                 Streamlit Dashboard
```

---

# ⚙️ Workflow

1. Network logs are received by the AI agent.
2. Gemini analyzes the incoming traffic.
3. Suspicious behavior is classified.
4. The agent decides the appropriate response.
5. High-risk IP addresses can be blocked automatically.
6. Critical incidents are escalated to a human analyst.
7. Prompt injection attempts are intercepted before execution.

---

# 🧩 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Agent Framework | Google ADK |
| LLM | Gemini 1.5 Pro |
| UI | Streamlit |
| Data Format | JSON |
| Tool Calling | MCP |
| Development | Antigravity IDE |

---

# 📂 Project Structure

```
ThreatShield-AI/
│
├── app.py
├── agent.py
├── tools.py
├── prompts.py
├── requirements.txt
├── README.md
│
├── images/
│   ├── dashboard.png
│   └── guardrails.png
│
└── sample_logs/
```

---

# 🛠️ Local Setup

Clone the repository

```bash
git clone https://github.com/yourusername/ThreatShield-AI.git

cd ThreatShield-AI
```

Install dependencies

```bash
uv sync
```

Run the application

```bash
uv run streamlit run app.py
```

---

# 🧪 Development Commands

```bash
# Validate agent configuration
agents-cli lint

# Run local playground
agents-cli playground

# Execute evaluation tests
agents-cli eval
```

---

# 🛡️ Security Features

- Prompt Injection Detection
- Safe Tool Invocation
- Structured MCP Tool Calls
- Controlled Firewall Actions
- Human Approval for Critical Cases

---

# 🎯 Future Improvements

- Live SIEM Integration
- VirusTotal API Support
- Multi-Agent Collaboration
- Email & Slack Alerts
- Threat Intelligence Integration
- Interactive Analytics Dashboard

---

# 📹 Demo Video

> Add your YouTube or Google Drive link here.

---

# 👨‍💻 Author

**Harshit Sharma**

AI & Machine Learning Developer

Built using **Google ADK**, **Gemini 1.5 Pro**, **Antigravity IDE**, and **Streamlit**.

---

# 📄 License

This project was created for the **Google Kaggle AI Agents: Intensive Vibe Coding Capstone Project** for educational and demonstration purposes.
