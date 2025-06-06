def calculate_expression(expr):
    try:
        return eval(expr)
    except Exception:
        return "Invalid expression"
