# Activity 6: Exception Handling
import os
#parent class
class BasicCalculator:
    def __init__(self):
        self.result = 0

#for additional
    def clear(self): #clear the screen import os?
        os.system('cls' if os.name == 'nt' else 'clear')

    def header(self): #display the header
        print("*" * 25)
        print("SIMPLE CALCULATOR".center(25))
        print("*" * 25)

#operations
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("You cannot divide by nothing bro!")
        return num1 / num2

if __name__ == "__main__":
    calc = calculation()
    calc.run()
