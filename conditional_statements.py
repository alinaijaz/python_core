marks = int(input("Enter your marks: "))
# if
if marks >= 50:
    print("Pass")
# if-else
if marks >= 50:
    print("Pass")
else:
    print("Fail")
# if-elif-else
if marks >= 80:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")

# Nested if
if marks >= 50:
    if marks >= 80:
     print("Excellent")
    else:
        print("Good")