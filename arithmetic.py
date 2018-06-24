"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    result = (num1 + num2)
    return answer


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    result = num1 - num2
    return result


def multiply(num1, num2):
    """Multiply the two inputs together."""
    result = num1 * num2
    return result


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    if num2 == 0:
        print ("Cannot divide by 0")
        return
    else:
        result = num1/num2
        return result

def square(num1):
    """Return the square of the input."""
    result = num1 ** 2
    return result

def cube(num1):
    """Return the cube of the input."""
    result = num1 ** 3
    return result


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    result = num1 ** num2
    return result

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    result = num1 % num2
    return result