
def add(n1: int | float, n2: int | float) -> int| float:
    """Add two ints/floats together."""
    return n1 + n2

def subtract(n1: int | float, n2: int | float) -> int | float:
    """Subtract one int/float from another."""
    return n1 - n2

def multiply(n1: int | float, n2: int | float) -> int | float:
    """Multiply two ints/floats."""
    return n1 * n2

def divide(n1: int | float, n2: int | float) -> int | float:
    """Divide one int/float by another."""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(operations["*"](4, 8))