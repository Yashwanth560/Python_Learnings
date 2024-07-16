def calculator():
    try:
        number1=int(input("enter the number: "))
        number2=int(input("enter the number: "))
        operation=input("enter operation(+, -, *, /): ")
        if operation=="+":
            result=number1+number2
        elif operation=="-":
            result=number1-number2
        elif operation=="*":
            result=number1*number2
        elif operation=="/":
            result=number1/number2
        else:
            print("invalid input")
        print(f"The result is : {result}")
     
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except ValueError:
        print("Invalid")
calculator()
    


       