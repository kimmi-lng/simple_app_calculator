# Activity 6: Exception Handling

# Instructions:
# - Do the programming exercises in module 3 page 21.
# - Upload your code in a new GitHub repository.
# - Git commit on every milestone, part of your grade is based on your git commit. 
# - Code should be OOP and have inheritance implementation
# - Feel free to add anything that will make your program maangas
# - Create a demo vid
# - Send me the link of your GitHub repo and demo before May 9
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

#child class
class calculation(BasicCalculator):
    def __init__(self):
        super().__init__() 
#use try and exept to ask for users inputs and see errors
    def get_operation(self):
    def get_numbers(self):
    def run(self): #will be used to run everything

