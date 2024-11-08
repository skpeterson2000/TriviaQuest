import tkinter as tk

def open_help_page(root):
    help_window = tk.Toplevel(root)
    help_window.title("Help/Tutorial")
    help_window.geometry("500x500")
    help_window.configure(bg="lightblue")

    label = tk.Label(help_window, text="Help/Tutorial coming soon enough!", bg="lightblue", fg="black", font=("Arial", 24))
    label.pack(pady=50)
