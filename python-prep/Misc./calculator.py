#!python
import sys

class MyCalculator:
    
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2 
    
    def add(self):
        val1_input = int(input("Enter your first value: "))
        val2_input = int(input("Enter your second value: "))
        return f"{val1_input + val2_input}"
    
    def subtract(self):
        val1_input = int(input("Enter your first value: "))
        val2_input = int(input("Enter your second value: "))
        return val1_input - val2_input

    def multiply(self):
        val1_input = int(input("Enter your first value: "))
        val2_input = int(input("Enter your second value: "))
        return val1_input * val2_input
    
    def divide(self):
        val1_input = int(input("Enter your first value: "))
        val2_input = int(input("Enter your second value: "))
        return val1_input / val2_input


if __name__ == "__main__":
    val1_input = int(input("Enter your first value: "))
    val2_input = int(input("Enter your second value: "))
    calc = MyCalculator(val1_input, val2_input)
    print(calc.add())
    print("Done")