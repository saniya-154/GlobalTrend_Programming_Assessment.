#Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).
class Operations:
    def __init__(self):
        self.a = int(input("Enter a first number: "))
        self.b = int(input("Enter a second number: "))
        self.operator = input("Enter the operation to be performed (+, -, *, /): ")

    def arithmetic_operations(self):
        if self.operator == "+":
            return self.a + self.b
        elif self.operator == "-":
            return self.a - self.b
        elif self.operator == "*":
            return self.a * self.b
        elif self.operator == "/":
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operator. Please use +, -, *, or /."

# Example usage
operation_instance = Operations()
result = operation_instance.arithmetic_operations()
print(f"Result: {result}")