import tkinter as tk
from tkinter import ttk
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def calculations(days, minTemp, maxTemp, sports, swim, events):
    # Perform calculations based on the input
    bottoms = math.ceil(days / 3)
    tops = math.ceil(days / 1.3)
    jumpers = math.ceil(days / 3)
    dresses = math.ceil(days / 3)
    bras = math.ceil(days / 3)
    socks = math.ceil(days + 1)
    pants = math.ceil(days * 1.3)
    pyjamas = math.ceil(days / 3)
    others = ""

    if minTemp > 20:
        jumpers -= 1
    else:
        jumpers += 1
    if swim == "Yes":
        others = others + "\nSwimsuit"
    if sports == "Yes":
        others = others + "\nSports outfit"
    if events == "Yes":
        others = others + "\nEvents outfit"
    if maxTemp > 23:
        others = others + "\nSuncream"
    result = f"\nBottoms: {bottoms}\nTops: {tops}\nJumpers: {jumpers}\nDresses: {dresses}\nBras: {bras}\nSocks: {socks}\nPants: {pants}\nPyjamas: {pyjamas}\nOthers: {others}"

    return result


def decideShoes(maxTemp, sports, events):
    shoes = "Vejas"
    if maxTemp > 25:
        shoes = shoes + "\nSandals"

    if sports == "Yes":
        shoes = shoes + "\nTrainers"

    if events == "Yes":
        shoes = shoes + "\nHeels"
    result = f"\n{shoes}"
    return result


def decideSkincareMakeup(days, events):
    if days > 3:
        skincare = f"\nMoisturizer \nToner \nExfoliant \nSPF \nRetinol \nFacewash \nMask"
    else:
        skincare = f"\nMoisturizer \nToner \nSPF \nFacewash"
    if events == "Yes":
        makeup = f"\nFull face"
    else:
        makeup = f"\nMinimal"

    results = skincare + makeup
    return results


def generate_packing_list():
    days = int(int_entry.get())
    minTemp = int(range_start_entry.get())
    maxTemp = int(range_end_entry.get())
    sports = dropdown1.get()
    swim = dropdown2.get()
    events = dropdown3.get()
    results = calculations(days, minTemp, maxTemp, sports, swim, events)
    shoes = decideShoes(maxTemp, sports, events)
    skincare_makeup = decideSkincareMakeup(days, events)
    create_checklist(results, shoes, skincare_makeup, "checklist.pdf")

    # Create a new window for displaying the result
    result_window = tk.Toplevel(root)
    result_window.title("Packing List")

    # Display the result
    result_label = ttk.Label(result_window, text="Packing List: {}".format(results))
    result_label.pack()

    # Generate PDF Button
    pdf_button = ttk.Button(result_window, text="Generate PDF", command=lambda: create_checklist(results, shoes, skincare_makeup, "checklist.pdf"))
    pdf_button.pack()

    # Close button for the result window
    close_button = ttk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack()


def create_checklist(clothes, shoes, skincare_makeup, filename):
    # Create a PDF file
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font size and line height
    font_size = 12
    line_height = font_size + 4

    # Define titles and their formatting
    titles = {
        "Clothes": ("Helvetica-Bold", 14),
        "Shoes": ("Helvetica-Bold", 14),
        "Skincare and Makeup": ("Helvetica-Bold", 14)
    }

    # Create a formatted checklist PDF
    y = 750  # Initial y-coordinate
    for title, content in zip(titles.keys(), [clothes, shoes, skincare_makeup]):
        # Draw title
        title_font, title_size = titles[title]
        c.setFont(title_font, title_size)
        c.drawString(50, y, f"{title}:")
        y -= line_height

        # Draw content
        content_lines = content.split('\n')
        c.setFont("Helvetica", font_size)
        for line in content_lines:
            if line.strip():  # Exclude empty lines
                c.drawString(70, y, f"- {line.strip()}")
                y -= line_height

        # Add extra space after each section
        y -= line_height

    # Save the PDF file
    c.save()


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
dropdown1 = ttk.Combobox(root, values=["Yes", "No"])
dropdown1.pack()

dropdown2_label = ttk.Label(root, text="Swimming?")
dropdown2_label.pack()
dropdown2 = ttk.Combobox(root, values=["Yes", "No"])
dropdown2.pack()

dropdown3_label = ttk.Label(root, text="Fancy events?")
dropdown3_label.pack()
dropdown3 = ttk.Combobox(root, values=["Yes", "No"])
dropdown3.pack()

# Generate Packing List Button
generate_button = ttk.Button(root, text="Generate Packing List", command=generate_packing_list)
generate_button.pack()

root.mainloop()

