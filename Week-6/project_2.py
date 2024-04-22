from tkinter import *
from tkinter import messagebox

    
def comp_sci():
    
    def submit2():
        frame = Toplevel()
        frame.title("Requirements")
        frame.geometry("500x200")
        print(grades)

        jamb_score = jamb_score_entry.get()
        jamb = int(jamb_score)
        grade = grades
        interview = interview_entry.get()
        info = Label(frame, text=f"You got a jamb score of {jamb_score}")
        info.pack()
        j = 0
        for i in subjects:
            if jamb > 300 and "no" in credit and interview == "yes":
                info1 = Label(frame, text=f"Your grade for {i} is {grade[j]}")
                info1.pack()
            j += 1
        else:
            print("YYY")
    


    window = Tk()
    window.title("Requirements")
    window.geometry("500x200")

    
    
    jamb_score_label = Label(window, text="Jamb Score")
    jamb_score_label.pack()
    jamb_score_entry = Entry(window)
    jamb_score_entry.pack()

    instruct = Label(window, text= "Enter the grades obtained for the following courses:")
    instruct.pack()

    subjects = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]
    
    credit = []
    grades = []
    for i in subjects:
        subject_label = Label(window, text= i)
        subject_label.pack()
        
        subject_entry = Entry(window)
        subject_entry.pack()
        subject = subject_entry.get().upper()
        
        if subject in ["A1", "B2", "B3", "C4", "C5", "C6"]:
            credit.append("yes")
            grades.append(subject)
        else:
            credit.append("no")
    
    interview_label = Label(window, text="Did you pass the interview \n Enter yes or no")
    interview_label.pack()
    interview_entry = Entry(window)
    interview_entry.pack()

    submit_button = Button(window, text="Submit", command=submit2)
    submit_button.pack()

    window.mainloop()

    
# Creating the conditionals
def submit():
    department = department_entry.get().lower()
    if department == "computer science":
        comp_sci()
    # elif department == "mass communication":
    #     mass_com()
    else:
        messagebox.error("Error", "Department entered does not exist")

# Create username label and entry
root = Tk()
root.title("Main Window")
root.geometry("500x200")

name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

department_label = Label(root, text="Department:")
department_label.pack()
department_entry = Entry(root)
department_entry.pack()

submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()