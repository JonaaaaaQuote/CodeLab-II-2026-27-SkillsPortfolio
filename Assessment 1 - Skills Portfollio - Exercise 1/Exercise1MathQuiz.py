import tkinter as tk
from tkinter import *
import random

root = tk.Tk()

# Page Settings
root.geometry("520x420")
root.title("Math Quiz")
root.configure(bg="#1e1e2e")

# Difficulty Levels List


difficultylevels = {
    1: ("Easy", 1, 9),
    2: ("Medium", 10, 99),
    3: ("Hard", 100, 9999)
}


# Variables
totalquestions = 10
fpoints = 10
spoints = 5

# Changable Variables

score = 0
questionno = 0
attempt = 1
answer = 0
low = 1
high = 9


# Clear Screen Function


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Start Page


def start_page():
    clear_screen()

    Label1 = tk.Label(root, text="Math Quiz", font=("Segoe UI", 50, "bold"),
                      bg="#1e1e2e", fg="#f5f5f5")
    Label1.pack(pady=(90, 0))

    button1 = tk.Button(root, text="Start Quiz", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                        fg="#f5f5f5", command=difficulty_level_screen)
    button1.pack(padx=20, pady=0)

# Difficulty Level Screen


def difficulty_level_screen():
    clear_screen()

    Label1 = tk.Label(root, text="Choose Your Difficulty", font=("Segoe UI", 30, "bold"),
                      bg="#1e1e2e", fg="#f5f5f5")
    Label1.pack(pady=(10, 20))

    gridframe = tk.Frame(root, bg="#1e1e2e")
    gridframe.pack()

    easy = tk.Button(gridframe, text="1. Easy", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                     fg="#f5f5f5", width=15, height=1, command=lambda: startquiz(difficultylevels[1][1], difficultylevels[1][2]))
    easy.grid(row=0, column=1, padx=15, pady=15)

    medium = tk.Button(gridframe, text="2. Medium", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                       fg="#f5f5f5", width=15, height=1, command=lambda: startquiz(difficultylevels[2][1], difficultylevels[2][2]))
    medium.grid(row=1, column=1, padx=15, pady=15)

    hard = tk.Button(gridframe, text="3. Hard", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                     fg="#f5f5f5", width=15, height=1, command=lambda: startquiz(difficultylevels[3][1], difficultylevels[3][2]))
    hard.grid(row=2, column=1, padx=15, pady=15)


# Quiz logic function


def startquiz(min_num, max_num):
    global low, high, score, questionno
    global info, question, entry, feedback

    low = min_num
    high = max_num
    score = 0
    questionno = 0

# Quiz Screen
    clear_screen()

    info = tk.Label(root, font=("Segoe UI", 20, "bold"),
                    bg="#1e1e2e", fg="#b9b9d0")
    info.pack(pady=(30, 20))

    question = tk.Label(root, font=("Segoe UI", 30, "bold"),
                        bg="#1e1e2e", fg="#f5f5f5")
    question.pack(pady=(10))

    entry = tk.Entry(root, font=("Segoe UI", 20, "bold"),
                     bg="#1e1e2e", fg="#f5f5f5", width=10, justify="center")
    entry.pack(pady=(10))
    entry.bind("<Return>", lambda event: checkanswer())

    submit = tk.Button(root, text="Submit", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                       fg="#f5f5f5", width=12, command=checkanswer)
    submit.pack(pady=(10))

    feedback = tk.Label(root, font=("Segoe UI", 20, "bold"),
                        bg="#1e1e2e", fg="#f5f5f5")
    feedback.pack(pady=(10))

    questiongen()

# Question Formulation With List


def questiongen():
    global questionno, attempt, answer
    questionno = questionno + 1

    if questionno > totalquestions:
        results()
        return

    num1 = random.randint(low, high)
    num2 = random.randint(low, high)
    operation = random.choice(['+', '-'])

    if operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    attempt = 1

    info.config(
        text=f"Question {questionno} of {totalquestions}  Score: {score}")
    question.config(text=f"{num1} {operation} {num2} = ?")
    feedback.config(text="")
    entry.delete(0, tk.END)
    entry.focus()

    # Answer Checking Function


def checkanswer():
    global score, attempt

    try:
        user_answer = int(entry.get())
    except ValueError:
        feedback.config(text="Please enter a valid number.")
        entry.delete(0, tk.END)
        return

    if user_answer == answer:
        if attempt == 1:
            score = score + fpoints
        else:
            score = score + spoints
        questiongen()

    elif attempt == 1:
        feedback.config(text="Try again")
        attempt = 2
        entry.delete(0, tk.END)
    else:
        questiongen()


def results():
    clear_screen()

    if score > 90:
        rank = "A+ Excellent"

    elif score > 80:
        rank = "A Very Good"

    elif score > 70:
        rank = "B Good"

    elif score > 60:
        rank = "C Average"

    elif score > 50:
        rank = "D Poor"

    elif score > 40:
        rank = "F Fail"

    tk.Label(root, text="Quiz Completed", font=("Segoe UI", 30, "bold"),
             bg="#1e1e2e", fg="#f5f5f5").pack(pady=(30, 20))

    tk.Label(root, text=f"Score: {score}", font=("Segoe UI", 30, "bold"),
             bg="#1e1e2e", fg="#f5f5f5").pack(pady=10)

    tk.Label(root, text=f"Rank: {rank}", font=("Segoe UI", 30, "bold"),
             bg="#1e1e2e", fg="#f5f5f5").pack(pady=10)

    tk.Button(root, text="Restart Quiz", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
              fg="#f5f5f5", width=15, command=start_page).pack(pady=(20, 5))

    tk.Button(root, text="Quit", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
              fg="#f5f5f5", width=15, command=root.destroy).pack(pady=(5))


start_page()
root.mainloop()
