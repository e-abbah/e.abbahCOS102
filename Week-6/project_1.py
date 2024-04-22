from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

def welcomeMessage(cost, location):
    # Create a Tkinter window
    window = Toplevel(root)
    window.config(bg="grey")
    window.title("Price of delivery")
    window.geometry("500x200")

    label_1 = Label(window, text=f"Dear Customer,\n")
    label_1.pack()
    label_2 = Label(window, text=f"The cost of delivery to {location} is N{cost}")
    label_2.pack()

    # Run the Tkinter event loop
    root.mainloop()

def submit():
    weight = int(weight_entry.get())
    location = (location_entry.get()).lower()
    
    if weight >= 10 and location == "ibeju-lekki":
        cost = 5000
        welcomeMessage(cost, location)
    elif weight < 10 and location == "ibeju_lekki":
        cost = 3500
        welcomeMessage(cost, location)
    elif weight >= 10 and location == "epe":
        cost = 10000
        welcomeMessage(cost, location)
    elif weight < 10 and location == "epe":
        cost = 5000
        welcomeMessage(cost, location)
    
    else:
        messagebox.showerror("Check!", "Invalid Weight or location")

# Create a main window
root = Tk()
root.config(bg="gold")
root.title("Cost of delivery")
root.geometry("500x200")

# Create  a username label and entry
weight_label = Label(root, fg="brown", text="Weight:")
weight_label.pack()
weight_entry = Entry(root)
weight_entry.pack()

# Create a location label and entry
location_label = Label(root, text="location")
location_label.pack()
location_entry = Entry(root)
location_entry.pack()

# Create a submit button
submit_button = Button(root, text="Check Price", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()








  