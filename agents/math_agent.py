from tools.calculator import calculate_expression
from gemini_integration import query_gemini
import re

class MathAgent:
    def answer(self, question): #"solve", "force", "gravity",
        match = re.search(r"(\d+\s*[\+\-\*/]\s*\d+)", question) # search question give solve 1 + 2
        if match:
            result = calculate_expression(match.group(1))
            return f"The result is: {result}"
        return query_gemini(question)