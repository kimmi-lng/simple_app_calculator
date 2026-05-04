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
        print("Select operation:")
        print("[1] Add")
        print("[2] Subtract")
        print("[3] Multiply")
        print("[4] Divide") 
        operation = input("Enter choice (1-4): ")
        if operation not in ['1', '2', '3', '4']:
            raise ValueError("Invalid operation choice!")
        return operation
    
    def get_numbers(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            raise ValueError("Invalid input! Enter numeric values.")
        
    def run(self): #will be used to run everything
        while True:
            self.clear()
            self.header()
            try:
                operation = self.get_operation()
                num1, num2 = self.get_numbers()
                if operation == '1':
                    self.result = self.add(num1, num2)
                elif operation == '2':
                    self.result = self.subtract(num1, num2)
                elif operation == '3':
                    self.result = self.multiply(num1, num2)
                elif operation == '4':
                    self.result = self.divide(num1, num2)

                print(f"\nResult: {self.result}")

            except ValueError as e:
                print(f"Input error occurred: {e}")
            except ZeroDivisionError as e:
                print(f"Math error occurred: {e}")

            again = input("\nDo you want to perform another calculation? (y/n): ")
            if again.lower() != 'y':
                print("\nThank you!")
                break

if __name__ == "__main__":
    app = calculation()
    app.run()
