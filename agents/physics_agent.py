from tools.physics_constants import get_constant
from gemini_integration import query_gemini

class PhysicsAgent:
    def answer(self, question):
        constant = get_constant(question)
        if constant:
            return f"The value is: {constant}"
        return query_gemini(question)