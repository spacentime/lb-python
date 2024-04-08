class Calculator:        
    def add(self, x, y, doPrint = False):
        """Addition method."""
        result = x + y
        if doPrint:
            print('{} + {} = {}'.format(x, y, result))
        return result

    def subtract(self, x, y):
        """Subtraction method."""
        return x - y

    def multiply(self, x, y):
        """Multiplication method."""
        return x * y

    def divide(self, x, y):
        """Division method."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
