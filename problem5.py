no_of_classes_attended=int(input("The number of classes attended: "))
no_of_classes_held=int(input("The number of classes held: "))

percentage=(no_of_classes_attended/no_of_classes_held)*100

print("The percentage of attendance:", percentage)

if percentage>=75:
    print("The student is allowed to sit in exam")
else:
    print("Your attendance is low. So you are not allowed")
