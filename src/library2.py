import tkinter as tk
from library import start_category_selection

def start_game():
    start_category_selection()

def open_settings():
    print("Settings")  # Placeholder for settings functionality

def gather_player_info():
    print("Player Info")  # Placeholder for gathering player information

def show_leaderboard():
    print("Leaderboard")  # Placeholder for leaderboard functionality

def close_app():
    root.destroy()

def start_home_page():
    root = tk.Tk()
    root.title("Prepared for ∞")
    root.geometry("900x600")
    root.configure(bg="#11137e")

    home_label = tk.Label(root, text="Welcome to Prepared for ∞", font=("Arial", 24), bg="#11137e", fg="white")
    home_label.pack(pady=20)

    intro_text = tk.Label(root, text="Prepare yourself for an exciting journey...", font=("Arial", 14), bg="#11137e", fg="white")
    intro_text.pack(pady=10)

    button_frame = tk.Frame(root, bg="#11137e")
    button_frame.pack(pady=20, expand=True)

    # First row of buttons
    row1 = tk.Frame(button_frame, bg="#11137e")
    row1.pack(pady=5)

    start_button = tk.Button(row1, text="Start Game", command=start_game, bg="#00d32b", fg="white")
    start_button.pack(side=tk.LEFT, padx=10)

    settings_button = tk.Button(row1, text="Settings", command=open_settings, bg="#00d32b", fg="white")
    settings_button.pack(side=tk.LEFT, padx=10)

    player_info_button = tk.Button(row1, text="Player Info", command=gather_player_info, bg="#00d32b", fg="white")
    player_info_button.pack(side=tk.LEFT, padx=10)

    # Second row of buttons
    row2 = tk.Frame(button_frame, bg="#11137e")
    row2.pack(pady=5)

    leaderboard_button = tk.Button(row2, text="Leaderboard", command=show_leaderboard, bg="#00d32b", fg="white")
    leaderboard_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(row2, text="Exit", command=close_app, bg="#8e0000", fg="white")
    exit_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    start_home_page()
