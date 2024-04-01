print("Do you want to use cubic calculator or Quartic or Quadratic equation calculator?")

choice = input(" \n Enter cubic for Cubic equation calculator or quar for quartic equation and quad for Quadratic equation calculator  ")
if choice == "cubic":
    a = float(input("Enter the coefficient of x^3 "))
    b = float(input("Enter the coefficient of x^2 "))
    c = float(input("Enter the coefficient of x "))
    d =  float(input("Enter the constant of the equation "))
    roots = []

    for x in range(-100, 100):
        e = (a * pow(x, 3)) + (b * pow(x, 2)) + c * x + d
        if e == 0:
            roots.append(x)
    print(f"The roots of the equation are {roots} ")


elif choice == "quar":
    a = float(input("Enter a"))
    b = float(input("Enter b"))
    c = float(input("Enter c"))
    d = float(input("Enter d"))
    e = float(input("Enter e"))

    roots = []

    for x in range(-100, 100):
        h = (a * (x ** 4)) + (b * (x ** 3)) + c * (x ** 2) + d*x + e
        if h == 0:
            roots.append(x)
    print(f"The roots of the equation are {roots} ")

    



elif choice == "quad":
    a = int(input("Enter the a(coefficient of x^2) of the equation "))
    b = int(input("Enter the b( coefficient of x) of the equation "))
    c = int(input("Enter the c(constant) of the equation "))

    import math
    d = (b) ** 2 - 4 * a * c
    det = math.sqrt(d)

    x1 = (- b + det ) / 2 * a
    x2 = (- b - det ) / 2 * a

    print(f"The first root is {x1} ")
    print(f"The second root is {x2} ")

else:
    print("Option not valid")


