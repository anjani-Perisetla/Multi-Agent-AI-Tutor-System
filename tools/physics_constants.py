constants = {
    "speed of light": "3.0 x 10^8 m/s",
    "gravitational constant": "6.674 x 10^-11 N·m²/kg²"
}

def get_constant(query):
    for key in constants:
        if key in query.lower():
            return constants[key]
    return None