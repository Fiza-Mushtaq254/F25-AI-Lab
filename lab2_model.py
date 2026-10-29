
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = "IDLE"
    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if target_mode == self.previous_mode:
            command = "No command"
        else:
            command = "Send command"

        old_mode = self.previous_mode
        self.previous_mode = target_mode
        return old_mode, target_mode, command
agent = ClassroomAgent()
percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False),
    (29, False)
]
print("Classroom Agent Trace")
for step, percept in enumerate(percepts, 1):
    previous, target, command = agent.act(*percept)
    print("\nStep:", step)
    print("Previous mode:", previous)
    print("Percept:", percept)
    print("Target mode:", target)
    print("Command:", command)

