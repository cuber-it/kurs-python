# dialog.py
import tkinter as tk
from tkinter import simpledialog

def ask(prompt, default=""):
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Input", prompt, initialvalue=default)

name = ask("Name?", "Max")
print(name)
