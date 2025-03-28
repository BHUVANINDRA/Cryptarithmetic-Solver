import itertools

def is_valid_solution(mapping, equation):
    """Check if the given letter-to-digit mapping satisfies the equation."""
    for letter, digit in mapping.items():
        equation = equation.replace(letter, str(digit))
    
    left, right = equation.split("=")
    return eval(left) == eval(right)

def solve_cryptarithmetic(equation):
    """Solve a cryptarithmetic puzzle given as a string equation."""
    letters = set(filter(str.isalpha, equation))
    if len(letters) > 10:
        raise ValueError("Too many unique letters (>10), unsolvable with unique digits 0-9.")
    
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != 0 for word in equation.replace("=", "+").split("+")):
            if is_valid_solution(mapping, equation):
                return mapping
    return None

if __name__ == "__main__":
    puzzle = "SEND + MORE = MONEY"
    puzzle = puzzle.replace(" ", "")
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        print("Solution:", solution)
    else:
        print("No solution found.")
