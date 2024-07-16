# Accepting marks for 5 subjects from the user
sub1 = float(input("Enter marks for sub 1 (for 100): "))
sub2 = float(input("Enter marks for sub 2 (for 100): "))
sub3 = float(input("Enter marks for sub 3 (for 100): "))
sub4 = float(input("Enter marks for sub 4 (for 100): "))
sub5 = float(input("Enter marks for sub 5 (for 100): "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total_marks / 500) * 100

print(f"Marks for sub 1: {sub1}")
print(f"Marks for sub 2: {sub2}")
print(f"Marks for sub 3: {sub3}")
print(f"Marks for sub 4: {sub4}")
print(f"Marks for sub 5: {sub5}")

print(f"Total marks: {total_marks}")

print(f"Percentage: {percentage:.2f}%")
