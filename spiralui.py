#!python3

import tkinter as tk
from tkinter import messagebox
import copy

def convLine(s, m):
    convspam = ''
    for i in range(s-1):
        convspam += str(m[i]).center(len(str(s*s))) + ' '
    convspam += str(m[-1]).center(len(str(s*s)))
    return convspam

def newMt(mxs):
    spiralmx = []
    for x in range(mxs):
        spiralmx.append([])
        for y in range(mxs):
            spiralmx[x].append(0)
    return spiralmx

def spiralMx(mxs):
    mx0 = newMt(mxs)
    spmt = copy.deepcopy(mx0)
    flag = 1
    t = 0
    while flag <= mxs * mxs:
        for cl in range(t, mxs-t):
            spmt[t][cl] = flag
            flag += 1
        for rw in range(t+1, mxs-t):
            spmt[rw][mxs-1-t] = flag
            flag += 1
        for cl in range(mxs-2-t, t-1, -1):
            spmt[mxs-1-t][cl] = flag
            flag += 1
        for rw in range(mxs-2-t, t, -1):
            spmt[rw][t] = flag
            flag += 1
        t += 1
    return spmt

def generate_matrix():
    try:
        mxs = int(entry.get())
        if mxs <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return
        spmx = spiralMx(mxs)
        result_text.delete(1.0, tk.END)
        for i in range(mxs):
            cvdmx = convLine(mxs, spmx[i])
            result_text.insert(tk.END, cvdmx + '\n')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Spiral Matrix Generator")

# Create and place the widgets
tk.Label(root, text="Enter the size of the matrix:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Matrix", command=generate_matrix)
generate_button.pack(pady=10)

result_text = tk.Text(root, height=20, width=50)
result_text.pack(pady=10)

# Start the main event loop
root.mainloop()