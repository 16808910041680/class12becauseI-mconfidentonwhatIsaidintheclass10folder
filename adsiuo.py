print ("Hi! This is a function that... Well, it's a calculator.")
print ("Please enter the first number: ")
num1 = int(input())
print ("Please enter the second number: ")
num2 = int(input())
print ("Please enter the operation you want to do: ")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
op = int(input())
print ("Yes, this is a weak calculator. I know.")
def calc(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    else:
        return "Invalid operation"
print ("Calculating...")
result = calc(num1, num2, op)
print ("The result is: " + str(result))
