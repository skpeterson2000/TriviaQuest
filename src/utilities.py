import json
import tkinter as tk

def load_settings(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Settings file {filepath} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}.")
        return {}

def create_button(parent, text, command, bg_color, active_color):
    button = tk.Button(parent, text=text, command=command, bg=bg_color, fg="white", activebackground=active_color, activeforeground="black")
    button.pack(side=tk.LEFT, padx=10)
    button.bind("<Enter>", lambda e: button.config(bg=active_color))
    button.bind("<Leave>", lambda e: button.config(bg=bg_color))
    return button
