import mymodule

try:
    number1=int(input("enter the number: "))
    number2=int(input("enter the number: "))
    operation=input("enter operation(+, -, *, /): ")
    if operation=="+":
        mymodule.sum(number1,number2)
    elif operation=="-":
         mymodule.subtraction(number1,number2)
    elif operation=="*":
         mymodule.multiplication(number1,number2)
    elif operation=="/":
         mymodule.division(number1,number2)
    else:
        print("invalid input") 
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("Invalid")