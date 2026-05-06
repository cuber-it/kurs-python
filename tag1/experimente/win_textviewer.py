import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Viewer")

text = tk.Text(root, wrap="word")
text.pack(fill="both", expand=True)

def oeffnen():
    path = filedialog.askopenfilename()
    if path:
        text.delete("1.0", "end")
        text.insert("end", open(path).read())

tk.Button(root, text="Öffnen", command=oeffnen).pack()
root.mainloop()
