# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
firstNum = float(input("First Number: "))
secondNum = float(input("Second Number: "))
operation = input("Operation: ")
def calc(num1, num2, operation):
    if operation == "add":
        return firstNum + secondNum
    elif operation == "subtract":
        return firstNum - secondNum
    
print(calc(firstNum, secondNum, operation))