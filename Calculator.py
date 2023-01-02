import math
print("Welcome to Calculator")
print("Select your option")
print(" 1 : Addition ")
print(" 2 : Subtraction ")
print(" 3 : Multiplication ")
print(" 4 : Division ")
print(" 5 : Trigonometric Ratios ")
print(" 6 : Degree ")
print(" 7 : Radian ")
print(" 8 : Module(Remainder) ")
print("9. Square Root")
print("10. Power")
choice = input("Enter your choice:")

if choice == '1':
    num1 = float(input("Enter 1st number :"))
    num2 = float(input("Enter 2nd number :"))
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    num1 = float(input("Enter 1st number :"))
    num2 = float(input("Enter 2nd number :"))
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    num1 = float(input("Enter 1st number :"))
    num2 = float(input("Enter 2nd number :"))
    print(num1, "x", num2, "=", num1 * num2)
elif choice == '4':
    num1 = float(input("Enter 1st number :"))
    num2 = float(input("Enter 2nd number :"))
    print(num1, "/", num2, "=", num1 / num2)
elif choice == '8':
    num1 = int(input("Enter 1st number :"))
    num2 = int(input("Enter 2nd number :"))
    print(num1, "%", num2, "=", num1 % num2)
elif choice == "9":
    num = int(input("Enter number: "))
    print("The square root is %f " %(math.sqrt(num)) )
elif choice == "10": 
    num = int(input("Enter number: "))
    print("The power is %d " %(math.pow(num, 2)) )
  # Trigo

elif choice == '5':
    x = int(input("Enter the angle :"))
    y = math.radians(x)
    print(" 1 : Sin ")
    print(" 2 : Cos ")
    print(" 3 : Tan ")
    choice1 = input("Enter your choice:")
    if choice1 == '1':
        print("sin ", x, "=", (math.sin(y)))
    if choice1 == '2':
        print("cos ", x, "=", (math.cos(y)))
    if choice1 == '3':
        print("tan ", x, "=", (math.tan(y)))

# Radian

pi = 22/7
radian = float(input("Input radians: "))
degree = radian*(180/pi)
print(degree)

# Degree
pi = 22/7
degree = float(input("Input degree: "))
radian = degree*pi/180
print(radian)

