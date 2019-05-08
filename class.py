option = """
    Choices :
            "+" Addition
            "-" Subtraction
            "*" Multiplication
            "/" Division
            "%" Modulus
            "**" Exponent
            "sqrt" SqureRoot
"""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return int(self.num1 + self.num2)

    def subtraction(self):
        return int(self.num1 - self.num2)

    def multiplication(self):
        return int(self.num1 * self.num2)

    def division(self):
        return int(self.num1 / self.num2)

    def modulus(self):
        return int(self.num1 % self.num2)

    def exponent(self):
        return int(self.num1 ** self.num2)

    def square_root(self):
        return int(sqrt(self.num1))

if __name__ == "__main__":
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        print(option)
        operator = input("Mathematical operator: ")

        obj = Calculator(num1,num2)

        if operator == "+":
            print ("The Sum {} and {} is: ".format(num1,num2), obj.addition())
        elif operator == "-":
            print ("The Diffirence {} and {} is: ".format(num1,num2), obj.subtraction())
        elif operator == "*":
            print ("The Product {} and {} is: ".format(num1,num2), obj.multiplication())
        elif operator == "/":
            print ("The Quotient {} and {} is: ".format(num1,num2), obj.division())
        elif operator == "%":
            print("The remainder of {} and {} is: ".format(num1, num2), obj.modulus())
        elif operator == "**":
            print("The squared of {} and {} is:".format(num1, num2), obj.exponent())
        elif operator == "sqrt":
            try:
                print("The SquareRoot of num1({}) is {}.".format(num1), obj.square_root())
            except:
                print("Num1({}) doesn't have a SquareRoot.".format(num1))
        else:
            print("Invalid operator")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")