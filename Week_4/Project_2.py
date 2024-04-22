
# IZifin Technology

experience = int(input("How many years of experience do you have? "))
age = int(input("What's your age?"))

if experience > 25 and age >= 55:
    print('The annual ATR is: N5,600,000')
elif experience > 20 and age >= 45:
    print('The annual ATR is: N4,480,000')
elif experience > 10 and age >= 35:
    print('The annual ATR is: N1,500,000')
elif experience <= 10 and age < 35:
    print('The annual ATR is: N550,000')
else:
    print("No annual ATR for this annual experience and age")

