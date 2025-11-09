import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Enter Details")
root.geometry("400x300")
root.config(bg="#1a1818")

title_label = tk.Label(root, text="User Information Form", font=("Arial", 16, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="#f2f2f2")
name_label.pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

email_label = tk.Label(root, text="Enter your email:", font=("Arial", 12), bg="#f2f2f2")
email_label.pack(pady=(10, 0))
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

def on_submit():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        messagebox.showinfo("Success", f"Hello {name}! Your email '{email}' is saved.")
    else:
        messagebox.showwarning("Warning", "Please fill in all fields!")

submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=on_submit)
submit_btn.pack(pady=20)

root.mainloop()
