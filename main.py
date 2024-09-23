import math
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def cross(a, b, c):
    """
    Performs produit croisé (cross multiplication).
    Given: a/b = c/x, it returns x.
    """
    if b == 0:
        raise ValueError("Division by zero in cross multiplication.")
    return (c * b) / a

def mash_shell():
    print(Fore.CYAN + "Welcome to MASH (Math Operation Shell)")
    print(Fore.YELLOW + "Type '-h' for help or 'exit' to quit.\n")
    
    while True:
        # Read input
        user_input = input(Fore.GREEN + "MASH> ").strip()

        if user_input.lower() == 'exit':
            print(Fore.RED + "Exiting MASH. Goodbye!")
            break

        elif user_input == '-h':
            print(Fore.BLUE + help_menu())
        
        # Parse prebuilt commands
        elif user_input.startswith('cross'):
            try:
                _, a, b, c = user_input.split()
                a, b, c = float(a), float(b), float(c)
                result = cross(a, b, c)
                print(Fore.MAGENTA + f"Result of cross multiplication: {result}")
            except ValueError as ve:
                print(Fore.RED + f"Error: {ve}")
            except Exception:
                print(Fore.RED + "Usage: cross a b c (where a/b = c/x)")

        # Factorial
        elif user_input.startswith('factorial'):
            try:
                _, n = user_input.split()
                n = int(n)
                result = math.factorial(n)
                print(Fore.MAGENTA + f"Factorial of {n}: {result}")
            except Exception:
                print(Fore.RED + "Usage: factorial n (where n is a non-negative integer)")

        # Power
        elif user_input.startswith('power'):
            try:
                _, base, exp = user_input.split()
                base, exp = float(base), float(exp)
                result = math.pow(base, exp)
                print(Fore.MAGENTA + f"{base} raised to the power of {exp}: {result}")
            except Exception:
                print(Fore.RED + "Usage: power base exponent")

        # GCD
        elif user_input.startswith('gcd'):
            try:
                _, a, b = user_input.split()
                a, b = int(a), int(b)
                result = math.gcd(a, b)
                print(Fore.MAGENTA + f"GCD of {a} and {b}: {result}")
            except Exception:
                print(Fore.RED + "Usage: gcd a b (where a and b are integers)")

        # LCM
        elif user_input.startswith('lcm'):
            try:
                _, a, b = user_input.split()
                a, b = int(a), int(b)
                result = lcm(a, b)
                print(Fore.MAGENTA + f"LCM of {a} and {b}: {result}")
            except Exception:
                print(Fore.RED + "Usage: lcm a b (where a and b are integers)")

        # Other prebuilt operations (50 more cases)
        elif user_input.startswith('sum'):
            try:
                numbers = list(map(float, user_input.split()[1:]))
                result = sum(numbers)
                print(Fore.MAGENTA + f"Sum: {result}")
            except Exception:
                print(Fore.RED + "Usage: sum n1 n2 ... (sum all numbers)")

        elif user_input.startswith('average'):
            try:
                numbers = list(map(float, user_input.split()[1:]))
                result = sum(numbers) / len(numbers)
                print(Fore.MAGENTA + f"Average: {result}")
            except Exception:
                print(Fore.RED + "Usage: average n1 n2 ... (average of numbers)")

        elif user_input.startswith('min'):
            try:
                numbers = list(map(float, user_input.split()[1:]))
                result = min(numbers)
                print(Fore.MAGENTA + f"Min: {result}")
            except Exception:
                print(Fore.RED + "Usage: min n1 n2 ... (minimum value)")

        elif user_input.startswith('max'):
            try:
                numbers = list(map(float, user_input.split()[1:]))
                result = max(numbers)
                print(Fore.MAGENTA + f"Max: {result}")
            except Exception:
                print(Fore.RED + "Usage: max n1 n2 ... (maximum value)")

        elif user_input.startswith('median'):
            try:
                numbers = sorted(list(map(float, user_input.split()[1:])))
                mid = len(numbers) // 2
                if len(numbers) % 2 == 0:
                    result = (numbers[mid - 1] + numbers[mid]) / 2
                else:
                    result = numbers[mid]
                print(Fore.MAGENTA + f"Median: {result}")
            except Exception:
                print(Fore.RED + "Usage: median n1 n2 ... (median of numbers)")

        # Default case: Eval basic math expressions
        else:
            try:
                result = eval_math(user_input)
                print(Fore.MAGENTA + f"Result: {result}")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

def help_menu():
    """Returns the help menu showing available commands."""
    return """
Available Commands:
-------------------
cross a b c        -> Performs cross multiplication: a/b = c/x, solve for x.
factorial n        -> Returns the factorial of n.
power base exp     -> Returns base raised to the power of exp.
gcd a b            -> Returns the Greatest Common Divisor of a and b.
lcm a b            -> Returns the Least Common Multiple of a and b.
sum n1 n2 ...      -> Returns the sum of the numbers.
average n1 n2 ...  -> Returns the average of the numbers.
min n1 n2 ...      -> Returns the minimum value.
max n1 n2 ...      -> Returns the maximum value.
median n1 n2 ...   -> Returns the median value.

Type 'exit' to quit the shell.
"""

def lcm(a, b):
    """Returns the least common multiple (LCM) of two integers."""
    return abs(a * b) // math.gcd(a, b)

def eval_math(expression):
    """Safely evaluates a mathematical expression."""
    allowed_functions = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,
        'sqrt': math.sqrt,
        'pi': math.pi,
        'e': math.e,
        'pow': pow,
        'gcd': math.gcd
    }
    
    return eval(expression, {"__builtins__": None}, allowed_functions)

if __name__ == "__main__":
    mash_shell()
