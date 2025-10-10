"""
Command Line Interface for Calculator
Example: python -m src.cli add 5 3
"""
import sys
import os
import click

# Add the parent directory to Python path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'power':
            result = power(num1, num2)
        elif operation in ('square_root', 'sqrt'):
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result nicely
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")
            
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    calculate()