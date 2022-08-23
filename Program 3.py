''' PROGRAM 3: Write a menu driven program to calculate the area of different shapes using functions '''

def square(n):
    print(f"Area of square with side {n} =",n*n)

def circle(n):
    print(f"Area of circle with radius {n} =",3.14*n*n)

def rectangle(n, m):
    print(f"Area of rectangle with length {n} and breadth {m} =",n*m)

def triangle(n, m):
    print(f"Area of triangle with side length {n} and height {m} =",0.5*n*m)

def mendr():
    shapeinput = str(input("\n\nOptions -\n\n=) Square\n\n=) Circle\n\n=) Rectangle\n\n=) Triangle\n\n=) Exit\n\n Enter the shape you want to calculate the area of: "))
    if shapeinput.lower() == 'square':
        n = float(input("Enter the side length: "))
        square(n)
    if shapeinput.lower() == 'circle':
        n = float(input("Enter the radius of the circle: "))
        circle(n)
    if shapeinput.lower() == 'rectangle':
        n = float(input("Enter the length of the circle: "))
        m = float(input("Enter the breadth of the circle: "))
        rectangle(n,m)
    if shapeinput.lower() == 'triangle':
        n = float(input("Enter the side length of the triangle: "))
        m = float(input("Enter the height of the triangle: "))
        triangle(n,m)
    if shapeinput.lower() == 'exit':
        print("Program terminated")

mendr()

''' SAMPLE OUTPUT REMINDER. FOR THIS ONE MAKE SURE YOU WRITE A SAMPLE OUTPUT FOR AREAS OF ALL SHAPES '''