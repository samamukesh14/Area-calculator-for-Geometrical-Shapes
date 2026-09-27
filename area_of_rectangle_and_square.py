# to calculate the area of a rectangle or square

print("A. Rectangle")
print("B. Square")
option = input("take option A or B: ")

if option == "A":
    l = int(input("enter the length :"))
    b = int(input("enter the breadth :"))
    Area = l * b
    print("The area of rectangle is", Area, "sq")
elif option == "B":
    S = int(input("enter the side length :"))
    Area = S * S
    print("The area of square", Area, "sq")
else:
    print("take option A or B")
  
