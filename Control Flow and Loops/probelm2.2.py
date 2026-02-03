num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 
opration = input("Enter operation (+, -, *, /): ")

match opration:
    case "+" :
        print("Addition:", num1 + num2)
    case "-" :
        print("Subtraction:", num1 - num2)
    case "*" :
        print("Multiplication:", num1 * num2)
    case "/" :
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")