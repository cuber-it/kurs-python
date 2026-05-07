import tkinter as tk
from tkinter import messagebox

def ausgabe(*args, sep=" ", end="\n"):
  text = sep.join(str(a) for a in args) + end
  messagebox.showinfo("Ausgabe", text)

print = ausgabe

if __name__ == "__main__":
  ausgabe("Hello", "world")

  wert = 3.14
  ausgabe("PI:", wert)

  tag = 6
  monat = 5
  jahr = 2026

  ausgabe(jahr, monat, tag, sep="-")
