from tkinter import *
from tkinter import messagebox

# Evaluate the criteria for computer science

def sorry():
    messagebox.showerror("info", "Sorry you do not meet up with the requirements")
def comp_science():
    window = Tk()
    window.title("Requirements")
    window.geometry("500x200")

    jamb_score_label = Label(window, text="Jamb Score")
    jamb_score_label.pack()
    jamb_score_entry = Entry(window)
    jamb_score_entry.pack()
    
    label = Label(window, text="Enter grade attained for the following")
    label.pack()
    
    subject_label1 = Label(window, text="English")
    subject_label1.pack()
    subject_entry1 = Entry(window)
    subject_entry1.pack()
    

    subject_label2 = Label(window, text="Math")
    subject_label2.pack()
    subject_entry2 = Entry(window)
    subject_entry2.pack()
    
    subject_label3 = Label(window, text="Physics")
    subject_label3.pack()
    subject_entry3 = Entry(window)
    subject_entry3.pack()
    
    subject_label4 = Label(window, text="Chemistry")
    subject_label4.pack()
    subject_entry4 = Entry(window)
    subject_entry4.pack()
    

    subject_label5 = Label(window, text="Further Maths")
    subject_label5.pack()
    subject_entry5 = Entry(window)
    subject_entry5.pack()

    interview_label = Label(window, "Did you pass the interview \n Enter yes or no")
    interview_label.pack()
    interview_entry = Entry(window)
    interview_entry.pack()

    
    jamb_score = jamb_score_entry.get()
    interview = interview_entry.get()
    subject1 = subject_entry1.get()
    subject2 = subject_entry2.get()
    subject3 = subject_entry3.get()
    subject4 = subject_entry4.get()
    subject5 = subject_entry5.get()

    if jamb_score > 250 and subject1 == "A" or "B" or "C" and subject2 == "A" or "B" or "C" and subject3 == "A" or "B" or "C" and subject4 == "A" or "B" or "C" or subject5 == "A" or "B" or "C":
        su    
    
    
    window.mainloop()
    


def mass_com():
    window = Tk()
    window.title("Requirements")
    window.geometry("500x200")

    jamb_score_label = Label(window, text="Jamb Score")
    jamb_score_label.pack()
    jamb_score_entry = Entry(window)
    jamb_score_entry.pack()

    subjects = ["English", "Mathematics", "Literature", "Economics", "Government"]
    check = []
    grades = []
    nice = True
    bad = False
    for i in subjects:
        subject_label = Label(window, text=i)
        subject_label.pack()
        subject_entry = Entry(window)
        subject_entry.pack()
        subject = subject_entry.get().upper
        if subject == "A" or "B" or "C":
            check.append(nice)
            grades.append(subject)
        else:
            check.append(bad)
    interview_label = Label(window, "Did you pass the interview \n Enter yes or no")
    interview_label.pack()
    interview = Entry(window)
    interview.pack()
    interviewed = (interview.entry.get).lower()
    
    jamb_score = int(jamb_score_entry.get)
    if jamb_score >= 250 and bad not in check and interviewed == "yes":
        submit_button1 = Button(window, text="Submit", command=welcome)
        submit_button1.pack()

    window.mainloop()


# Evaluating if the course is computer science or mass communication

# Ask for department on a window
screen = Tk()
screen.title("data")
screen.geometry("300x200")

name_label = Label(screen, text="Name:")
name_label.pack()
name_entry = Entry(screen)
name_entry.pack()

department_label = Label(screen, text="Department:")
department_label.pack()
department_entry = Entry(screen)
department_entry.pack()

if department_entry == "Computer Science" or department_entry == "computer science" or department_entry == "Computer science":
    comp_science()
elif department_entry == "mass communication" or department_entry == "Mass Communication" or department_entry == "Mass communication":
    mass_com()
submit_button = Button(screen, text="Submit", command=submit)
submit_button.pack()

screen.mainloop()



# Ask if they got credit atleast in those courses
#  Ask if they passed interview