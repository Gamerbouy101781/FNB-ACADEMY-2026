print("======================================================")
operator = input("Choose operator (+ , -, x , /, //, %)\n= ")
print("")
num1 = float(input("Enter first number\n= "))
num2 = float(input("Enter second number\n= "))
print("======================================================")

if (operator == "+"):
    addition = num1 + num2
    print(f"{num1} + {num2} = {round(addition, 2)}")
    print("======================================================")
elif (operator == "-"):
    subtraction = num1 - num2
    print(f"{num1} - {num2} = {round(subtraction, 2)}")
    print("======================================================")
elif (operator == "x"):
    multiplication = num1 * num2
    print(f"{num1} x {num2} = {round(multiplication, 2)}")
    print("======================================================")
elif (operator == "/"):
    if (num2 == 0):
        print(f"{num1} cannot be divided by {num2}")
    else:
        division = num1 / num2
        print(f"{num1} / {num2} = {round(division, 2)}")
        print("======================================================")
elif (operator == "//"):
    if (num2 == 0):
        print(f"{num1} cannot be divided by {num2}")
    else:
        floor_division = num1 // num2
        print(f"{num1} // {num2} = {round(floor_division, 2)}")
        print("======================================================")
elif (operator == "%"):
    if (num2 == 0):
        print(f"{num1} cannot be divided by {num2}")
    else:
        modulus = num1 % num2
        print(f"{num1} % {num2} = {round(modulus, 2)}")
        print("======================================================")
else:
    print("Something went wrong!")
