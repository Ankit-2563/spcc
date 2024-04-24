class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, antecedent, consequent):
        self.rules.append((antecedent, consequent))

    def forward_chaining(self, initial_facts):
        inferred_facts = set(initial_facts)
        while True:
            new_facts = set()
            for rule in self.rules:
                if all(antecedent in inferred_facts for antecedent in rule[0]):
                    new_facts.add(rule[1])
            if not new_facts:
                break
            inferred_facts |= new_facts
        return inferred_facts

    def backward_chaining(self, goal, initial_facts):
        inferred_facts = set(initial_facts)
        agenda = [goal]
        while agenda:
            current_goal = agenda.pop()
            if current_goal in inferred_facts:
                continue
            is_proved = False
            for rule in self.rules:
                if rule[1] == current_goal:
                    if all(antecedent in inferred_facts for antecedent in rule[0]):
                        is_proved = True
                        break
                    else:
                        for antecedent in rule[0]:
                            agenda.append(antecedent)
            if is_proved:
                inferred_facts.add(current_goal)
        return inferred_facts

# Example usage:
kb = KnowledgeBase()
# Add rules to the knowledge base
kb.add_rule(['flu', 'cough'], 'fever')
kb.add_rule(['fever'], 'sickness')

# Forward chaining example
initial_facts = ['flu', 'cough']
forward_result = kb.forward_chaining(initial_facts)
print("Forward chaining result:")
print(forward_result)

# Backward chaining example
goal = 'sickness'
backward_result = kb.backward_chaining(goal, initial_facts)
print("\nBackward chaining result:")
print(backward_result)
