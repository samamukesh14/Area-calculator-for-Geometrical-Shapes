# Geometric Shape Area Calculator

def circle():
    print("\n Area of Circle")
    Radius = float(input("enter the radius of circle : "))
    Area = 3.14*(Radius**2)
    print("The area of circle ", Area , "sq")


def parallelogram_rhombus():
    print("\n first. Parallelogram")
    print("second. Rhombus")
    option = input("enter your option :")

    if option == "first":
        Base = int(input("enter the base : "))
        Height = int(input("enter the height : "))
        area = Base * Height
        print("The area of parallelogram", area , "sq")

    elif option == "second":
        Diagonal_1 = int(input("enter the first diagonal : "))
        Diagonal_2 = int(input("enter the second diagonal : "))
        Area = (Diagonal_1 * Diagonal_2)/2
        print("The area of rhombus", Area , "sq")

    else:
        print("Please enter first or second")


def rectangle_square():
    print("\n A. Rectangle")
    print("B. Square")
    option = input("enter your option : ")

    if option == "A":
        l = int(input("enter the length : "))
        b = int(input("enter the breadth : "))
        Area = l * b
        print("The area of rectangle", Area, "sq")

    elif option == "B":
        S = int(input("enter the side length : "))
        Area = S * S
        print("The area of square", Area, "sq")

    else:
        print("Please enter A or B")


def trapezoid():
    print("\n Area of Trapezoid")
    a = int(input("Enter the first parallel side of trapezoid :"))
    b = int(input("Enter the second parallel side of trapezoid :"))
    Height = float(input("Enter the height of trapezoid :"))
    Area = ((a + b) * Height)/2
    print("The area of trapezoid ", Area, "sq")


def triangle():
    print("\n Area of Triangle")
    Base = int(input("enter the base of triangle :"))
    Height = int(input("enter the height of triangle :"))
    Area = (Base * Height)/2
    print("The area of triangle", Area, "sq")


while True:
    print("\n===============================")
    print("Geometric Shape Area Calculator")
    print("=============================")
    print("1. Circle")
    print("2. Parallelogram and Rhombus")
    print("3. Rectangle and Square")
    print("4. Trapezoid")
    print("5. Triangle")
    print("6. Exit")

    option = input("enter your option: ")

    if option == "1":
        circle()

    elif option == "2":
        parallelogram_rhombus()

    elif option == "3":
        rectangle_square()

    elif option == "4":
        trapezoid()

    elif option == "5":
        triangle()

    elif option == "6":
        print("Thank you!")
        break

    else:
        print("Please enter a valid option")

    input("\n Press enter to continue...")
