import tkinter as tk
# from main import main as start_romans_road

def start_category(category):
    print(f"Starting category: {category}")  # Placeholder for other categories

def return_home():
    root.destroy()  # Adjust this to correctly return to your Home page

root = tk.Tk()
root.title("Category Selection")
root.geometry("1024x600")
root.configure(bg="#11137e")

title_label = tk.Label(root, text="Select a Category", font=("Arial", 24), bg="#11137e", fg="white")
title_label.pack(pady=20)

categories_frame = tk.Frame(root, bg="#11137e")
categories_frame.pack(pady=20, expand=True)

categories = [
    "Romans Road",
    "Faith Heroes",
    "Old Testament",
    "New Testament",
    "God used men",
    "Jesus",
    "Commandments",
    "Psalms",
    "Proverbs",
    "Beatitudes",
    "Epistles",
    "Prophets"
]

buttons = []
row, col = 0, 0

for category in categories:
    if category == "Romans Road":
        button = tk.Button(categories_frame, text=category, command=start_romans_road, bg="#1c9431", fg="white", width=20)
    else:
        button = tk.Button(categories_frame, text=category, command=lambda c=category: start_category(c), bg="#1c9431", fg="white", width=20)
    button.grid(row=row, column=col, padx=10, pady=10)
    buttons.append(button)
    
    col += 1
    if col >= 4:  # New row after 4 columns
        col = 0
        row += 1

# Frame to hold the buttons
button_frame = tk.Frame(root, bg="#11137e")
button_frame.pack(pady=(50, 0))  # Adjust '50' to move the buttons up or down

# Create buttons and pack them with side=tk.LEFT and padx/pady for padding
exit_button = tk.Button(button_frame, text="EXIT", command=return_home, bg="#8e0000", fg="white")
exit_button.pack(side=tk.LEFT, padx=10, pady=20)

home_button = tk.Button(button_frame, text="HOME", command=return_home, bg="#3c4056", fg="white")
home_button.pack(side=tk.LEFT, padx=10, pady=20)

# Only one mainloop call
root.mainloop()
