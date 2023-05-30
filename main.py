import tkinter as tk
from tkinter import ttk
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def calculations(days):
    # Perform calculations based on the input     
    bottoms = math.ceil(days/3)
    tops = math.ceil(days/1.3)
    jumpers = math.ceil(days/3)
    dresses = math.ceil(days/3)
    bras = math.ceil(days/3)
    socks = math.ceil(days +1)
    pants = math.ceil(days *1.3)
    pyjamas = math.ceil(days/3)
    result = f"\nBottoms: {bottoms}\nTops: {tops}\nJumpers: {jumpers}\nDresses: {dresses}\nBras: {bras}\nSocks: {socks}\nPants: {pants}\nPyjamas: {pyjamas}"

    return result 

def create_checklist(days, filename):
    # Call the calculations function to get the variable values
    variables = calculations(days)

    # Split the variables string into a list of lines
    lines = variables.split('\n')

    # Create a PDF file
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font size and line height
    font_size = 12
    line_height = font_size + 4

    # Create a formatted checklist PDF
    y = 750  # Initial y-coordinate
    for line in lines:
        c.setFont("Helvetica", font_size)
        c.drawString(50, y, f"- {line} [ ]")
        y -= line_height

    # Save the PDF file
    c.save()


def submit():
    days = int(int_entry.get())
    range_start = int(range_start_entry.get())
    range_end = int(range_end_entry.get())
    dropdown1_value = dropdown1.get()
    dropdown2_value = dropdown2.get()
    dropdown3_value = dropdown3.get()
    results = calculations(days)
    create_checklist(days, "checklist.pdf")
    # Create a new window for displaying the result
    result_window = tk.Toplevel(root)
    result_window.title("Packing List")
    
    # Display the result
    result_label = ttk.Label(result_window, text="Packing List: {}".format(results))
    result_label.pack()
    
    # Close button for the result window
    close_button = ttk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack()

root = tk.Tk()
root.title("Holiday Information")

# Integer Input
int_label = ttk.Label(root, text="How many days is your holiday?:")
int_label.pack()
int_entry = ttk.Entry(root)
int_entry.pack()

# Integer Range Input
range_label = ttk.Label(root, text="Please enter the temperature range in C:")
range_label.pack()
range_frame = ttk.Frame(root)
range_frame.pack()
range_start_entry = ttk.Entry(range_frame, width=5)
range_start_entry.pack(side=tk.LEFT)
range_separator_label = ttk.Label(range_frame, text="-")
range_separator_label.pack(side=tk.LEFT)
range_end_entry = ttk.Entry(range_frame, width=5)
range_end_entry.pack(side=tk.LEFT)

# Dropdown Boxes
dropdown1_label = ttk.Label(root, text="Sporting/hiking activities?")
dropdown1_label.pack()
dropdown1 = ttk.Combobox(root, values=["Yes (one)", "Yes (many)", "No"])
dropdown1.pack()

dropdown2_label = ttk.Label(root, text="Swimming?")
dropdown2_label.pack()
dropdown2 = ttk.Combobox(root, values=["Yes", "No"])
dropdown2.pack()

dropdown3_label = ttk.Label(root, text="Fancy events?")
dropdown3_label.pack()
dropdown3 = ttk.Combobox(root, values=["Yes (one)", "Yes (many)", "No"])
dropdown3.pack()

# Submit Button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
