age=int(input("Enter your age: "))

if age>=18:
    print(f"Your age is {age} and you are eligible to vote")
else:
    print(f"Your age is {age} so you are not eligible")

#Percentage and Grading
percentage=int(input("Enter your percentage: "))

if percentage>75 and percentage<=100:
    print("O Grade")
elif percentage>60 and percentage<=75:
    print("A Grade")
elif percentage>50 and percentage<=60:
    print("B Grade")
else :
    print("C Grade")
