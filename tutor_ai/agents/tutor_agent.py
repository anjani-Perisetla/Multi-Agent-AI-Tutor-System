from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from gemini_integration import query_gemini

class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()

    def handle_question(self, question):
        subject = self.classify_subject(question)
        if subject == "math":
            return self.math_agent.answer(question)
        elif subject == "physics":
            return self.physics_agent.answer(question)
        else:
            return "Sorry, I can only help with Math and Physics."

    def classify_subject(self, question):
        keywords = {"math": ["solve", "equation", "add", "subtract"],
                    "physics": ["law", "force", "gravity", "energy"]}
        for subject, keys in keywords.items():
            if any(word in question.lower() for word in keys):
                return subject
        return "unknown"