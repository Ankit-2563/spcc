def eliminate_left_recursion(grammar):
    for A in list(grammar.keys()):
        productions_A = grammar[A]

        left_recursive_productions = [prod for prod in productions_A if prod.startswith(A)]
        non_left_recursive_productions = [prod for prod in productions_A if not prod.startswith(A)]

        if not left_recursive_productions:
            continue

        A_prime = A + "'"
        grammar[A_prime] = [prod[len(A):] + A_prime for prod in left_recursive_productions] + ["ε"]
        grammar[A] = [prod + A_prime for prod in non_left_recursive_productions]

    return grammar

def read_grammar_from_file(filename):
    grammar = {}
    with open('Grammar.txt', 'r') as file:
        for line in file:
            non_terminal, rhs = line.strip().split('->')
            grammar[non_terminal.strip()] = [symbol.strip() for symbol in rhs.split('|')]
    return grammar

if __name__ == "__main__":
    filename = 'Grammar.txt'
    print(f"Reading grammar productions from '{filename}':")
    user_grammar = read_grammar_from_file(filename)
    eliminated_grammar = eliminate_left_recursion(user_grammar)
    print("\nModified Grammar after eliminating left recursion:")
    for non_terminal, productions in eliminated_grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")
