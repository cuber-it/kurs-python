# dialog.py
import tkinter as tk
from tkinter import simpledialog

def ask(prompt, default=""):
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Input", prompt, initialvalue=default)

input = ask

if __name__ == "__main__":
    name = ask("Name?")
    print(name, type(name))
