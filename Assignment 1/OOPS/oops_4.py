class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is undefined."

calc = Calculator()
print(f"Addition: {calc.add(5, 3)}")
print(f"Subtraction: {calc.subtract(5, 3)}")
print(f"Multiplication: {calc.multiply(5, 3)}")
print(f"Division: {calc.divide(5, 0)}")
