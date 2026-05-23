from simple_calculator import BasicCalculator

class calculation(BasicCalculator): #use try and exept to ask for users inputs and see errors
    def __init__(self):
        super().__init__() #initialize the parent class

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