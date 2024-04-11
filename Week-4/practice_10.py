import tkinter as tk

from tkinter import messagebox

# Handling button click event
def button_click():
    #print("Button clicked!")

    # show an information from message box
    messagebox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

    # Ask for user confirmation
    result = messagebox.askyesno("COnfirmation", "Do you want to continue?")

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

# Add a label widget
label = tk.Label(root, text="Hello Friend \n")
label.pack()

# Add a button widget
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

# Styling the button widget
button.config(fg="red", bg="yellow")

# Start the event loop
root.mainloop()
