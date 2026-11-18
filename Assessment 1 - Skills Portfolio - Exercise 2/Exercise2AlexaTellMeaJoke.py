import tkinter as tk
import random
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "randomjokes.json")

root = tk.Tk()

root.geometry("700x420")
root.title("Joke")
root.configure(bg="#1e1e2e")


# ClearScreen


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def punchline(label, button, answer):
    label.configure(text=answer)
    button.place_forget()
# Function that moves the button randomly (extra)


def movebutton(event, button, moves):
    if moves["count"] > 0:
        moves["count"] -= 1
        maxx = root.winfo_width() - button.winfo_width()
        newx = random.randint(0, maxx)
        newy = random.randint(150, 260)
        button.place(x=newx, y=newy)


# Loads the jokes and punchlines from json file


def jokes(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["Jokes"]


jokeslist = jokes(JSON_PATH)

# Start page


def start_joke():
    clear_screen()

    Label1 = tk.Label(root, text="Joke Center", font=("Segoe UI", 50, "bold"),
                      bg="#1e1e2e", fg="#f5f5f5")
    Label1.pack(pady=(90, 0))

    button1 = tk.Button(root, text="Alexa... Tell Me a Joke", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                        fg="#f5f5f5", command=joke_screen)
    button1.pack(padx=20, pady=20)

# Joke Page


def joke_screen():
    clear_screen()

    joke = random.choice(jokeslist)

# Joke container
    Label2 = tk.Label(root, text=joke["Joke"], font=("Segoe UI", 20, "bold"),
                      bg="#1e1e2e", fg="#f5f5f5")
    Label2.pack(pady=(60, 20))

# Punchline Container
    Label3 = tk.Label(root, text="", font=("Segoe UI", 20, "italic"),
                      bg="#1e1e2e", fg="#f5f5f5")
    Label3.pack(pady=(10))

# Quit Button
    quitbutton = tk.Button(root, text="Quit", font=("Segoe UI", 13), bg="#6d4aff",
                           fg="#f5f5f5", command=root.destroy)
    quitbutton.pack(padx=20, pady=20)

# Next Joke Button
    nextbutton = tk.Button(root, text="Next", font=("Segoe UI", 15), bg="#6d4aff",
                           fg="#f5f5f5", command=joke_screen)
    nextbutton.pack(padx=20, pady=20)


# Punchline Button
    button2 = tk.Button(root, text="Show Punchline", font=("Segoe UI", 20, "bold"), bg="#6d4aff",
                        fg="#f5f5f5", command=lambda: punchline)
    button2.pack(padx=220, pady=200)

    button2.bind("<Enter>", lambda event: movebutton(event, button2, moves))


start_joke()
root.mainloop()
