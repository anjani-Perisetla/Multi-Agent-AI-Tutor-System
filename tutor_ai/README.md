# Multi-Agent AI Tutor System

This project implements a cloud-deployed, AI-powered tutoring system using the Gemini API and FastAPI. It features a main Tutor Agent that routes queries to domain-specific agents: Math Agent and Physics Agent.

## 🌐 Live Demo
- Deployed on: [https://your-app-url.railway.app](https://your-app-url.railway.app)

## 📁 Project Structure
- `main.py`: FastAPI app
- `agents/`: Tutor, Math, and Physics Agents
- `tools/`: Calculator and physics constant lookups
- `templates/` and `static/`: Frontend interface
- `.env`: API key storage

## 🚀 Setup Instructions
1. Clone repo: `git clone https://github.com/yourusername/tutor-ai`
2. Install dependencies: `pip install -r requirements.txt`
3. Add `.env` with your Gemini API key
4. Run app locally: `uvicorn main:app --reload`
5. Deploy to Railway

## 🔁 Agent Interaction
- Tutor Agent classifies query using keywords
- Routes to Math or Physics Agent
- Agents use tools or Gemini API for response

## 🛠️ Tools
- **Math**: Calculator for expressions
- **Physics**: Constant lookup (e.g., speed of light)

## ✅ Submission Links
- GitHub Repo: [https://github.com/yourusername/tutor-ai](https://github.com/yourusername/tutor-ai)
- Live App: [https://your-app-url.railway.app](https://your-app-url.railway.app)

## 💡 Challenges
- Managing subject classification accurately
- Handling Gemini API latency and errors

## 📜 License
MIT
