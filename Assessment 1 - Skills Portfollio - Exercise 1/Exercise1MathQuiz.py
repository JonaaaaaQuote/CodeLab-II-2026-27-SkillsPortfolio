import tkinter as tk
from tkinter import *

root = tk.Tk()

# Page Settings
root.geometry("520x420")
root.title("Math Quiz")
root.configure(bg="#1e1e2e")

# Start Page

Label1 = tk.Label(root, text="Math Quiz", font=("Segoe UI", 50, "bold"),
                  bg="#1e1e2e", fg="#f5f5f5")
Label1.pack(pady=(90, 0))


button1 = tk.Button(root, text="Start Quiz", font=("Segoe UI", 20), bg="#6d4aff",
                    fg="#f5f5f5",).pack(padx=20, pady=0)

# Difficulty Levels List
difficultylevels = {
    1: ("Easy", 1, 9),
    2: ("Moderate", 10, 99),
    3: ("Medium", 100, 999),
    4: ("Hard", 1000, 9999)
}

# Variables
totalquestions = 10
fpoints = 10
spoints = 5


root = mainloop()
