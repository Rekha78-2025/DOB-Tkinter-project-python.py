import tkinter as tk 

from tkinter import messagebox 

from datetime import datetime 

def calculate_age(): 
    dob_str = dob_entry.get() 
    
    try: 
        
        dob = datetime.strptime(dob_str,"%d-%m-%y") 
        today = datetime.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
        result_label.config(text=f"you are {age} years old.") 
    except ValueError: 
        
        result_label.config(text="please enter DOB in DD-MM-YYYY format.") 
        
        

root = tk.Tk() 
root.title("Age calculator") 
root.geometry("400x350") 
root.configure(bg="green") 

title = tk.Label(root, text="Age calculator", font=("Arial",16, "bold"), bg="white", fg="red") 
title.pack(pady=15) 

dob_label = tk.Label(root, text="enter date of birth(DD-MM-YYYY):", bg="white", fg="pink") 
dob_label.pack(pady=5) 

dob_entry = tk.Entry(root, font=("Arial", 12), justify="center") 
dob_entry.pack(pady=5) 

calculate_btn = tk.Button(root, text="calculate Age", command=calculate_age, bg="green", fg="white", font=("Arial, 12")) 
calculate_btn.pack(pady=10) 

result_label = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 14, "bold"), fg="#00529B")
result_label.pack(pady=10) 


root.mainloop()

