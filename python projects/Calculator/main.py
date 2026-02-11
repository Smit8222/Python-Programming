try :

    a =  int(input("Enter the 1st number :"))
    b = int(input("Enter the 2nd number :"))
    print("What kind of operation do you want to perform. Press + for addition \nPress - for subtraction \nPress * for multiplication \nPress / for division \nPress % for modulus ")
    o = input("Enter the operator :")
    match o :
        case "+" :
            print("The sum is : ",a+b)
        case "-" :
            print("The difference is : ",a-b)
        case "*" :
            print("The product is : ",a*b)
        case "/" :
            if b != 0 :
                print("The quotient is : ",a/b)
            else :
                print("Division by zero is not allowed")
        case "%" :
            if b != 0 :
                print("The modulus is : ",a%b)
            else :
                print("Modulus by zero is not allowed")

except ValueError :
    print("Please enter a valid number")