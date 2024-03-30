print("Do you want to use cubic calculator or Quadratic equation calculator?")

choice = input("Enter cubic for Cubic equation calculator and quad for Quadratic equation calculator  ")
if choice == "cubic":
    print("Underage")
    a = int(input("Enter the coefficient of x^3"))
    b = int(input("Enter the coefficient of x^2"))
    c = int(input("Enter the coefficient of x"))
    d =  int(input("Enter the constant of the equation"))

    Q = (3 * c - b ** 2)/9
    R = (9*b*c - 27*d - 2*(b**3))/54
    S = (R + ((Q ** 3 + R ** 2) ** 0.5)) ** 1/3
    T = (R - ((Q ** 3 + R ** 2) ** 0.5))** 1/3
    first_root = S + T - b /3
    second_root = -0.5 (S + T ) - (b/3) + 0.5





elif choice == "quad":
    a = int(input("Enter the a(coefficient of x^2) of the equation"))
    b = int(input("Enter the b( coefficient of x) of the equation"))
    c = int(input("Enter the c(constant) of the equation"))

    import math
    d = (b) ** 2 - 4 * a * c
    det = math.sqrt(d)

    x1 = (- b + det ) / 2 * a
    x2 = (- b - det ) / 2 * a

    print(f"The first value of x is {x1}")
    print(f"The second value of x is {x2}")

else:
    print("Option not valid")


