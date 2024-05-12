from tkinter import *
from tkinter import messagebox

def submit():
    def submit1():
        # Creating a function that calculates the order of the user
        calculator = 0
        entries = [category1_e, category2_e, category3_e, savoury_e, plant_e, vege_e, boiled_l_e, eba_e, poundo_e, semo_e, atama_e, egusi_e,
                chill_e, chicken_e, beef_e, fish_e, egg_e, sausage_e, water_e, glass_drink_e, pet1_e, pet2_e, can_e, fresh_e, pine_e, mango_e, zobo_e]

        list1 = [350, 350, 350, 350, 300, 150, 150, 150, 100, 100, 100, 450, 480, 1100, 400, 400, 500, 200, 200, 200, 150, 300, 350, 500, 600, 350,
                  350, 350]

        for i in range(len(entries)):
            itemss = entries[i].get()
            # Error handling if input is a string
            if type(itemss) == str:
                messagebox.showerror("Error handling", "You entered an Invalid input \n Kindly enter a valid quantity")
                break
            else:
                if itemss == "":
                    calculator += 0
                    listss = int(itemss)
                    cost1 = list1[i] * listss
                    calculator += cost1

        print(calculator)
        if calculator < 1000:
            discount = 0
            calculator -= discount
        elif calculator <= 2500:
            discount = 0.1 * calculator
            calculator -= discount
        elif calculator >= 2500 and calculator < 5000:
            discount = 0.15 * calculator
            calculator -= discount
        elif calculator > 5000:
            discount = 0.25 * calculator
            calculator -= discount


        window = Tk()
        window.geometry("200x100")
        name = name_e.get()
        label = Label(window, text=f"Dear {name}, \n The total amount of your order: \nN{calculator}")
        label.pack()

    # Placing entries and label at different part of the screen
    frame = Tk()
    frame.minsize(width=800, height=600)
    heading_l = Label(frame, text="PAU CAFETARIA", font=("times new roman", 20, "bold"), fg="black", bd=19, relief=GROOVE)
    heading_l.pack(fill=X)

    details = LabelFrame(frame, text="Details", font=("Arial", 15))
    details.pack(fill=X)
    name_l = Label(details, text="NAME:")
    name_l.grid(row=0, column=0, padx=20, pady=2)
    name_e = Entry(details, bd=7, width=20)
    name_e.grid(row=0, column=1, padx=8)

    #  For rice
    product1 = Frame(frame)
    product1.place(x=50, y=150) 
    category = LabelFrame(product1, text="RICE/PASTA", font=("TIMES", 10), fg="black")
    category.grid(row=0, column=0)

    category1_l = Label(category, text="Jollof Rice")
    category1_l.grid(row=0, column=0)
    category1_e = Entry(category, width=4)
    category1_e.grid(row=0, column=1)

    category2_l = Label(category, text="Coconut Fried Rice")
    category2_l.grid(row=1, column=0)
    category2_e = Entry(category, width=4)
    category2_e.grid(row=1, column=1)

    category3_l = Label(category, text="Jollof Spaghetti")
    category3_l.grid(row=2, column=0)
    category3_e = Entry(category, width=4)
    category3_e.grid(row=2, column=1)

    # For side dishes
    dish = LabelFrame(product1, text="SIDE DISHES", font=("TIMES", 10), fg="black")
    dish.grid(row=0, column=1)
    savoury_l = Label(dish, text="Savoury Beans")
    savoury_l.grid(row=0, column=0)
    savoury_e = Entry(dish, width=4)
    savoury_e.grid(row=0, column=1)

    roast_l = Label(dish, text="Roasted Sweet Potatoes")
    roast_l.grid(row=1, column=0)
    roast_e = Entry(dish, width=4)
    roast_e.grid(row=1, column=1)

    plant_l = Label(dish, text="Fried Plantains")
    plant_l.grid(row=2, column=0)
    plant_e = Entry(dish, width=4)
    plant_e.grid(row=2, column=1)

    vege_l = Label(dish, text="Mixed Vegetable Salad")
    vege_l.grid(row=3, column=0)
    vege_e = Entry(dish, width=4)
    vege_e.grid(row=3, column=1)

    boiled_l = Label(dish, text="Boiled Yam")
    boiled_l.grid(row=4, column=0)
    boiled_l_e = Entry(dish, width=4)
    boiled_l_e.grid(row=4, column=1)

    # For soup and Swallow
    soup = LabelFrame(product1, text="SOUP & SWALLOW", font=("TIMES", 10), fg="black")
    soup.grid(row=0, column=2)

    eba_l = Label(soup, text="Eba")
    eba_l.grid(row=0, column=0)
    eba_e = Entry(soup, width=4)
    eba_e.grid(row=0, column=1)

    poundo_l = Label(soup, text="Poundo Yam")
    poundo_l.grid(row=1, column=0)
    poundo_e = Entry(soup, width=4)
    poundo_e.grid(row=1, column=1)

    semo_l = Label(soup, text="Semo")
    semo_l.grid(row=2, column=0)
    semo_e = Entry(soup, width=4)
    semo_e.grid(row=2, column=1)

    atama_l = Label(soup, text="Atama Soup")
    atama_l.grid(row=3, column=0)
    atama_e = Entry(soup, width=4)
    atama_e.grid(row=3, column=1)

    egusi_l = Label(soup, text="Egusi Soup")
    egusi_l.grid(row=4, column=0)
    egusi_e = Entry(soup, width=4)
    egusi_e.grid(row=4, column=1)

    # For Proteins
    proteins = LabelFrame(product1, text="PROTEINS", font=("TIMES", 10), fg="black")
    proteins.grid(row=0, column=3)

    chill_l = Label(proteins, text="Sweet Chill Chicken")
    chill_l.grid(row=0, column=0)
    chill_e = Entry(proteins, width=4)
    chill_e.grid(row=0, column=1)

    chicken_l = Label(proteins, text="Grilled Chicken Beef")
    chicken_l.grid(row=1, column=0)
    chicken_e = Entry(proteins, width=4)
    chicken_e.grid(row=1, column=1)

    beef_l = Label(proteins, text="Fried Beef")
    beef_l.grid(row=2, column=0)
    beef_e = Entry(proteins, width=4)
    beef_e.grid(row=2, column=1)

    fish_l = Label(proteins, text="Fried Fish")
    fish_l.grid(row=3, column=0)
    fish_e = Entry(proteins, width=4)
    fish_e.grid(row=3, column=1)

    egg_l = Label(proteins, text="Boiled Egg")
    egg_l.grid(row=4, column=0)
    egg_e = Entry(proteins, width=4)
    egg_e.grid(row=4, column=1)

    sausage_l = Label(proteins, text="Sauteed Sausages")
    sausage_l.grid(row=5, column=0)
    sausage_e = Entry(proteins, width=4)
    sausage_e.grid(row=5, column=1)

    # For Beverages
    beverages = LabelFrame(product1, text="BEVERAGES", font=("TIMES", 10), fg="black")
    beverages.grid(row=0, column=4)

    water_l = Label(beverages, text="Water")
    water_l.grid(row=0, column=0)
    water_e = Entry(beverages, width=4)
    water_e.grid(row=0, column=1)

    glass_drink_l = Label(beverages, text="Glass Drink(35cl)")
    glass_drink_l.grid(row=1, column=0)
    glass_drink_e = Entry(beverages, width=4)
    glass_drink_e.grid(row=1, column=1)

    pet1_l = Label(beverages, text="Pet Drink(35cl)")
    pet1_l.grid(row=2, column=0)
    pet1_e = Entry(beverages, width=4)
    pet1_e.grid(row=2, column=1)

    pet2_l = Label(beverages, text="Pet Drink(50cl)")
    pet2_l.grid(row=3, column=0)
    pet2_e = Entry(beverages, width=4)
    pet2_e.grid(row=3, column=1)

    can_l = Label(beverages, text="Glass/Canned Malt")
    can_l.grid(row=4, column=0)
    can_e = Entry(beverages, width=4)
    can_e.grid(row=4, column=1)

    fresh_l = Label(beverages, text="Fresh Yo")
    fresh_l.grid(row=5, column=0)
    fresh_e = Entry(beverages, width=4)
    fresh_e.grid(row=5, column=1)

    pine_l = Label(beverages, text="Pineapple Juice")
    pine_l.grid(row=6, column=0)
    pine_e = Entry(beverages, width=4)
    pine_e.grid(row=6, column=1)

    mango_l = Label(beverages, text="Mango Juice")
    mango_l.grid(row=7, column=0)
    mango_e = Entry(beverages, width=4)
    mango_e.grid(row=7, column=1)

    zobo_l = Label(beverages, text="Zobo Drink")
    zobo_l.grid(row=8, column=0)
    zobo_e = Entry(beverages, width=4)
    zobo_e.grid(row=8, column=1)

    submit_button = Button(frame, text="CONTINUE \n TO PAY", command=submit1)
    submit_button.config(fg="gold", bg="red")
    submit_button.place(x=350, y=350)

    frame.mainloop()
# Creating the drop down menu
root = Tk()
root.minsize(width=500, height=700)



start = Label(text= "MENU", font=("Arial", 30, "bold"))
start.pack()
# Rice/Pasta
dish1 = Label(text="RICE/PASTA", font=("Arial", 12, "bold"))
dish1.place(x=50, y=70)
rice = {"Jollof Rice": 350, "Coconut Fried Rice":350, "Jollof Spaghetti": 350}
x1 = 10
y1 = 100
a1 = 150
for items in rice:
    food = Label(text= items)
    food.place(x=x1, y=y1)  
    amount = Label(text= rice[items])
    amount.place(x=a1, y=y1)
    y1 += 30
# Side Dishes
dish2 = Label(text="SIDE DISHES", font=("Arial", 12, "bold"))
dish2.place(x=20, y=200)
side = {"Savoury beans": 350, "Roasted Sweet Potatoes": 500, "Fried Plantains": 350, "Mixed Vegetable Salad": 150, "Boiled Yam": 150}
x2= 10
y2 = 230
a2 = 160
for items in side:
    food1 = Label(text= items)
    food1.place(x=x2, y=y2)
    amount1 = Label(text=side[items])
    amount1.place(x=a2, y=y2)
    y2 += 30
# Soup and Swallows
dish3 = Label(text="SOUP & SWALLOWS", font=("Arial", 12, "bold"))
dish3.place(x=20, y=400)
soup = {"Eba": 100, "Poundo Yam": 100, "Semo": 100, "Atama Soup":450, "Egusi Soup": 480}
x3 = 10
y3 = 430
a3 = 130
for items in soup:
    food2 = Label(text= items)
    food2.place(x=x3, y=y3)
    amount2 = Label(text = soup[items])
    amount2.place(x=a3, y=y3)
    y3 += 30

# Proteins
dish4 = Label(text="PROTEINS", font=("Arial", 12, "bold"))
dish4.place(x= 270, y=70)
proteins = {"Sweet Chill Chicken": 1100, "Grilled Chicken Wings": 400, "Fried Beef": 400, "Fried Fish": 500, "Boiled Egg": 200, "Sauteed Sausage": 200}
x4 = 250
y4 = 100
a4 = 360
for items in soup:
    food3 = Label(text= items)
    food3.place(x=x4, y=y4)
    amount3 = Label(text= soup[items])
    amount3.place(x= a4, y=y4)
    y4 += 30

# Beverages
dish5 = Label(text="BEVERAGES", font=("Arial", 12, "bold"))
dish5.place(x= 270, y=280)
beverages = {"Water": 200, "Glass Drink (35cl)": 150, "PET Drink (35cl)": 300, "PET Drink (50cl)": 350, "Glass/Canned Malt": 500, "Fresh Yo": 600, "Pineapple Juice": 350, "Mango Juice": 350, "Zobo Drink": 350}
x5 = 250
y5 = 310
a5 = 400
for items in beverages:
    food4 = Label(text = items)
    food4.place(x=x5, y=y5)
    amount4 = Label(text = beverages[items])
    amount4.place(x=a5, y=y5)
    y5 += 30

# Create submit button

submit_button = Button(root, text="ENJOY \n START ORDER", command=submit)
submit_button.config(fg="gold", bg="red")
submit_button.place(x=190, y=580)

root.mainloop()