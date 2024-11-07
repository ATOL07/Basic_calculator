print("Welcome to Basic Calculator Project")
print("Which option do you want to choose?")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("0.Exit")

option = int(input("Select an option for Basic Calculator Operation: "))

# Addition
if option == 1:
    n1 = int(input("Enter 1st Number: "))
    n2 = int(input("Enter 2nd Number: "))
    result = n1 + n2
    print("Addition is: " + str(result))

# Subtraction 
elif option == 2:
    n1 = int(input("Enter 1st Number: "))
    n2 = int(input("Enter 2nd Number: "))
    result = n1 - n2
    print("Subtraction is: " + str(result))


# Multiplication
elif option == 3:
    n1 = int(input("Enter 1st Number: "))
    n2 = int(input("Enter 2nd Number: "))
    result = n1 * n2
    print("Multiplication is: " + str(result))

# Division 
elif option == 4:
    n1 = int(input("Enter 1st Number: "))
    n2 = int(input("Enter 2nd Number: "))
    if n2 != 0:
        result = n1 / n2
        print("Division is: " + str(result))
    else:
        print("Error: Division by zero is not allowed.")

elif option == 0:
    print("Exiting the calculator. Goodbye!")

else:
    print("Invalid option. Please select a valid operation.")

