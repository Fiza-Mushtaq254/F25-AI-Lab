
class ReflexAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


class StatefulAgent:
    def __init__(self):
        self.previous_mode = "IDLE"

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        if target == self.previous_mode:
            command = "No command"
        else:
            command = "Send command"

        self.previous_mode = target
        return target, command


reflex = ReflexAgent()
stateful = StatefulAgent()
tests = [
    ("Hot room", 29, True, "COOL"),
    ("Repeated hot reading", 29, True, "COOL"),
    ("Boundary 20", 20, True, "IDLE"),
    ("Boundary 26", 26, True, "IDLE"),
    ("Cold room", 19, True, "WARM"),
    ("Empty room", 29, False, "ECO"),
    ("Repeated empty room", 29, False, "ECO")
]
print("Agent Comparison and Testing")
for name, temp, occupied, expected in tests:
    simple_result = reflex.act(temp, occupied)
    target, command = stateful.act(temp, occupied)
    print("\nTest:", name)
    print("Input:", (temp, occupied))
    print("Expected target:", expected)
    print("Reflex result:", simple_result)
    print("Stateful target:", target)
    print("Command:", command)
    print("Test passed:", target == expected)

