import sympy as sp
import re

print('Welcome to my wonderful shell! Type "exit" to quit. Made with ❤ by @thegoodduck')

def preprocess_expression(expression):
    # Sanitize input to replace non-standard minus signs with standard minus sign
    expression = expression.replace('−', '-')
    # Insert multiplication operator where needed
    expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
    expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
    expression = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expression)
    return expression

def solve_locally(expression):
    try:
        expression = preprocess_expression(expression)
        
        # Use regex to detect and split equations
        equation_pattern = re.compile(r'(.+?)\s*=\s*(.+)')
        equations = [equation_pattern.match(eq.strip()) for eq in expression.split(',')]
        
        if all(equations):
            eqs = [sp.Eq(sp.sympify(eq.group(1)), sp.sympify(eq.group(2))) for eq in equations]
            variables = list(set(re.findall(r'[a-zA-Z]', expression)))
            solution = sp.solve(eqs, variables)
            if not solution:
                return "The equation is always true (infinitely many solutions)"
            return solution
        else:
            expr = sp.sympify(expression)
            solution = sp.simplify(expr)
            return solution
    except Exception as e:
        return str(e)

def format_solution(solution):
    if isinstance(solution, dict):
        return ', '.join([f"{k} = {v}" for k, v in solution.items()])
    elif isinstance(solution, list):
        return ', '.join([str(s) for s in solution])
    return solution

def main():
    while True:
        user_input = input("Enter a math problem (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            # Try to solve locally
            local_solution = solve_locally(user_input)
            formatted_solution = format_solution(local_solution)
            print(f"Local solution: {formatted_solution}")
        except Exception as e:
            print(f"Local solving failed: {e}")

if __name__ == "__main__":
    main()
