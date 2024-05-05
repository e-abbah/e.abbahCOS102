from tkinter import *
from tkinter import messagebox

    
def comp_sci():
    
    def submit2():
        
        jamb_score = jamb_score_entry.get()
        jamb = int(jamb_score)
        interview = interview_entry.get()
        subject = subject_entry
        count = 0
        graded = []
        subjects = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]
        name = name_entry.get()
        for i in grades:
            grade = str(i.get()).upper()
            graded.append(grade)
        

            if grade in  ["A1", "B2", "B3", "C4", "C5", "C6"]:
                count += 1
            else:
                count += 0
        
        
        if jamb >= 250 and count == 5 and interview ==  "yes":
            
            messagebox.showinfo("Congratulations", "You have been admitted into PAU")

        else:
            messagebox.showinfo("Sorry", "You do not meet the admission requirement to PAU")
        frame = Toplevel()
        frame.title("Requirements")
        frame.geometry("500x200")
        last = Label(frame, text=f"Name: {name}")
        last.pack
        admitted = Label(frame, text=f"Jamb score: {jamb} \n Passed Interview: {interview}")
        admitted.pack()
        for i in range(5):
            admit = Label(frame, text=f"Grades in {subjects[i]}: {graded[i]}")
            admit.pack()

        

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
        grades.append(subject_entry)
        
        # if subject in ["A1", "B2", "B3", "C4", "C5", "C6"]:
        #     credit.append("yes")
        #     
        # else:
        #     credit.append("no")
    
    interview_label = Label(window, text="Did you pass the interview \n Enter yes or no")
    interview_label.pack()
    interview_entry = Entry(window)
    interview_entry.pack()

    submit_button = Button(window, text="Submit", command=submit2)
    submit_button.pack()

def mass_com():
    
    def submit2():
        
        jamb_score = jamb_score_entry.get()
        jamb = int(jamb_score)
        interview = interview_entry.get()
        subject = subject_entry
        count = 0
        graded = []
        subjects = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]
        name = name_entry.get()
        for i in grades:
            grade = str(i.get()).upper()
            graded.append(grade)
        

            if grade in  ["A1", "B2", "B3", "C4", "C5", "C6"]:
                count += 1
            else:
                count += 0
        
        
        if jamb >= 230 and count == 5 and interview ==  "yes":
            
            messagebox.showinfo("Congratulations", "You have been admitted into PAU")

        else:
            messagebox.showinfo("Sorry", "You do not meet the admission requirement to PAU")
        frame = Toplevel()
        frame.title("Requirements")
        frame.geometry("500x200")
        last = Label(frame, text=f"Name: {name}")
        last.pack
        admitted = Label(frame, text=f"Jamb score: {jamb} \n Passed Interview: {interview}")
        admitted.pack()
        for i in range(5):
            admit = Label(frame, text=f"Grades in {subjects[i]}: {graded[i]}")
            admit.pack()

        

    window = Tk()
    window.title("Requirements")
    window.geometry("500x200")

    
    
    jamb_score_label = Label(window, text="Jamb Score")
    jamb_score_label.pack()
    jamb_score_entry = Entry(window)
    jamb_score_entry.pack()

    instruct = Label(window, text= "Enter the grades obtained for the following courses:")
    instruct.pack()

    subjects = ["English", "Mathematics", "Economics", "Governement", "Lit in English"]
    
    credit = []
    grades = []
    for i in subjects:
        subject_label = Label(window, text= i)
        subject_label.pack()
        
        subject_entry = Entry(window)
        subject_entry.pack()
        grades.append(subject_entry)
        
        # if subject in ["A1", "B2", "B3", "C4", "C5", "C6"]:
        #     credit.append("yes")
        #     
        # else:
        #     credit.append("no")
    
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
    elif department == "mass communication":
        mass_com()
    else:
        messagebox.showerror("Error", "Department entered does not exist")

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