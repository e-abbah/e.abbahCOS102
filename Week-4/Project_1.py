import tkinter as tk
from tkinter import messagebox
#from PIL import Image, ImageTk

def welcomeMessage(username, others):
    # Create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x500")

    label_1 = tk.Label(window, text=f"GIG Logistics")
    label_1.pack()
    label_2 = tk.Label(window, text=f"Welcome {username} to the biometric software")
    label_2.pack()
    label_3 = tk.Label(window, text=f"Other People in this department are {others}")
    label_3.pack()

    # Run the Tkinter event loop
    root.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get()
    username1 = ""
    passwords = ""
    others = []


    users = {"Adeniran": "Logistics", "Adewunmi": "Accounting", "Adoh-Ajag": "Oshim", "Agbakuru": "Accounting", "Agbakwuru": "Logisitcs",
             "Akinde": "Accounting", "Arnika": "Logistics", "Atelly": "Delivery", "Azogu": "Delivery", "Beture": "Delivery", "Chukwuma" : "Logistics",
             "Ebi": "Accounting", "Egboro": "Administrator", "Ejidunmu": "Delivery", "Eleri": "Administration", "Eze": "Administration", "Ezeonye": "Logistics",
             "Giwa": "Logistics", "Icha": "Accounting", "Ikpati": "Accounting", "Iloenysi": "Delivery", "Iyawe": "Delivery", "Nwokolo": "Logistics",
             "Nwotokubo": "Logistics", "Obasogie": "Accounting", "Obi": "Accounting", "Obialor": "Accounting", "Ogbonna": "Delivery", "Oigbochie": "Delivery",
             "Okocha-Ojeah": "Administration", "Okolo": "Administration", "Okoro": "Logistics", "Olowokere": "Accounting", "Olubuade": "Accounting", "Osemeke": "Accounting",
            "Ossai": "Logistics", "Peter": "Logistics", "Quadri": "Delivery", "Ude-Ibe": "Delivery", "Umeh": "Administration"}
    for user in users:
        
        if password == users[user]:
            others.append(user)
            if username == user and password == users[user]:
                username1 += user
                passwords += password

    if username1 == username and passwords == password:
        if username in others:
            others.remove(username)
            welcomeMessage(username, others)
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create a main windowss
root = tk.Tk()
root.title("GIG Logistics")
root.geometry("500x500")

# Create  a username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create a password label and entry
password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the main event loop
root.mainloop()



