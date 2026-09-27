# area of parallelogram or rhombus

print("first. parallelogram")
print("second. rhombus")
option = input("take first or second option: ")

if option == "first":
    Base = int(input("enter the base :"))
    Height = int(input("enter the height :"))
    Area = Base * Height
    print("The area of parallelogram ", Area, "sq")
elif option == "second":
    Diagonal_1 = int(input("enter the first diagonal :"))
    Diagonal_2 = int(input("enter the second diagonal :"))
    Area = (Diagonal_1 * Diagonal_2) / 2
    print("The area of rhombus ", Area, "sq")
else:
    print("Please take first or second option")
