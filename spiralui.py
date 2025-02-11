#!python3

import tkinter as tk
from tkinter import messagebox, font
import spiralmx1  # Import the whole module

def calculate_text_size(mxs):
    """
    Calculate the appropriate text widget size based on matrix size.
    
    Args:
    mxs (int): Matrix size
    
    Returns:
    tuple: (width, height) in characters
    """
    # Calculate width based on the largest number (mxs*mxs) and spacing
    cell_width = len(str(mxs*mxs))
    total_width = (cell_width + 1) * mxs  # +1 for spacing
    # Height is matrix size plus some padding
    return (total_width + 2, mxs + 2)

def adjust_font_size(text_widget, mxs):
    """
    Adjust font size based on matrix size for better visibility.
    
    Args:
    text_widget: Tkinter Text widget
    mxs (int): Matrix size
    """
    base_size = 14
    if mxs > 10:
        base_size = max(8, int(base_size - (mxs-10)/2))
    custom_font = font.Font(family="Courier", size=base_size)
    text_widget.configure(font=custom_font)

def generate_matrix():
    """
    Generates the spiral matrix based on user input and displays it in the text widget.
    """
    try:
        mxs = int(entry.get())
        if mxs <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return
            
        # Calculate new dimensions
        width, height = calculate_text_size(mxs)
        
        # Reconfigure text widget
        result_text.configure(width=width, height=height)
        adjust_font_size(result_text, mxs)
        
        # Generate and display matrix using the module name
        spmx = spiralmx1.spiralMx(mxs)
        result_text.delete(1.0, tk.END)
        for i in range(mxs):
            cvdmx = spiralmx1.convLine(mxs, spmx[i])
            result_text.insert(tk.END, cvdmx + '\n')
            
        # Center the matrix content
        result_text.tag_configure("center", justify='center')
        result_text.tag_add("center", "1.0", "end")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def on_enter(event):
    generate_matrix()

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Spiral Matrix Generator")

# Configure main window
root.resizable(True, True)
root.minsize(300, 200)

# Create main frame with padding
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(expand=True, fill='both')

# Create and place the widgets
tk.Label(main_frame, text="Enter the size of the matrix:").pack(pady=5)
entry = tk.Entry(main_frame, width=10)
entry.pack(pady=5)
entry.bind("<Return>", on_enter)

generate_button = tk.Button(main_frame, text="Generate Matrix", command=generate_matrix)
generate_button.pack(pady=5)

exit_button = tk.Button(main_frame, text="Exit", command=exit_program)
exit_button.pack(pady=5)

# Create text widget with initial size
result_text = tk.Text(main_frame, width=20, height=10, font=("Courier", 12))
result_text.pack(expand=True, fill='both', pady=5)

# Start the main event loop
root.mainloop()