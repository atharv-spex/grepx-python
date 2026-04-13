#conditional statements classwork
name = input("enter the name:")
marks = float(input("enter the marks:"))
age =int(input("enter the age:"))
attendence = float(input("enter the attendance percentage:"))
has_id = input("do you have id:")
#if statements
if marks >= 40:
    print("you have passed")
#if-else
if attendence >= 75:
    print("Attendece ok!")
else:
    print("Attendece not ok!")

#if-elif-else
if marks>= 90:
    print("Grade A")
elif marks>= 80:
    print("Grade B")
elif marks>= 70:
    print("Grade C")
elif marks>= 60:
    print("Grade D")
else:
    print(" Fail ")
    print("grade =",grade)



#logical operators
if marks >= 40 and attendence >= 75 and has_id.lower() == "yes":
    print("you are allowed for final exam")
else:
    print("you are not allowed for final exam")

#chained comparison
if 18 <= age <= 25:
    print("age is valid student range")
else:
    print("age is not valid student range")

#ternary operator
result = "Pass" if marks >= 40 else "Fail"
print(" final result:", result)


