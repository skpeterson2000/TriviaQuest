import tkinter as tk
from game_logic import TriviaGame
from utilities import load_settings
#from help_page import HelpPage  # Import HelpPage for navigation

# Load settings from settings.json
settings = load_settings("config/settings.json")

def create_button(parent, text, command, bg_color, active_color):
    button = tk.Button(parent, text=text, command=command, bg=bg_color, fg="white", activebackground=active_color, activeforeground="black")
    button.pack(side=tk.LEFT, padx=10)
    button.bind("<Enter>", lambda e: button.config(bg=active_color))
    button.bind("<Leave>", lambda e: button.config(bg=bg_color))
    
    # Bind touchscreen events
    button.bind("<ButtonPress-1>", lambda e: button.invoke())
    button.bind("<ButtonRelease-1>", lambda e: button.invoke())

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title(settings["title"])
        self.root.geometry(settings["window_size"])
        self.root.configure(bg=settings["background_color"])

        welcome_label = tk.Label(root, text=settings["home_text"], font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        welcome_label.pack()

        text2_label = tk.Label(root, text="Prepared 4 \u221e - Home - ", wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        text2_label.pack(pady=10)

        psalm_label = tk.Label(root, text="                 Psalm 119:11\n I have hidden your word in my heart, that I might not sin against you. (NLT)", justify="left", wraplength=950, font=("Arial_Black", 18), bg=settings["background_color"], fg="gold")
        psalm_label.pack(pady=10)

        text3_label = tk.Label(root, text="This game is intended to be played in a group setting over a local network, but can also be played solitaire. Details on how to play, how to set up the game for a group setting can be found by clicking the Help/Tutorial section below.", wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        text3_label.pack(pady=10)

        intro_text = tk.Label(root, text=settings["intro_text"], font=("Arial", 14), bg=settings["background_color"], fg="gold")
        intro_text.pack(pady=10)

        button_frame = tk.Frame(root, bg=settings["background_color"])
        button_frame.pack(pady=15, expand=True)

        # First row of buttons
        row1 = tk.Frame(button_frame, bg=settings["background_color"])
        row1.pack(pady=5)

        create_button(row1, "Start Game", self.start_game, "#107b21", "#06e301")
        create_button(row1, "Leaderboard", self.show_leaderboard, "#817808", "#f6c909")
        create_button(row1, "Settings", self.open_settings, "#6c5400", "#ff8c00")
        create_button(row1, "Help/Tutorial", self.open_help, "#5e0e89", "#b654e9")

        # Second row of buttons
        row2 = tk.Frame(button_frame, bg=settings["background_color"])
        row2.pack(pady=15)

        create_button(row2, "Credits/About", self.show_credits, "#3c4056", "#c4cca6")
        create_button(row2, "Categories", self.show_categories, "#007ba7", "#00bfff")  # New Categories button
        create_button(row2, "Exit", self.exit_app, "#8e0000", "#ff1c1c")

    def start_game(self):
        self.root.destroy()
        game_window = tk.Tk()
        game = TriviaGame(game_window)
        game_window.mainloop()

    def show_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry(settings["window_size"])
        leaderboard_window.configure(bg=settings["background_color"])
        lbl = tk.Label(leaderboard_window, text="Leaderboard coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry(settings["window_size"])
        settings_window.configure(bg=settings["background_color"])
        lbl = tk.Label(settings_window, text="Settings page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def open_help(self):
        help_window = tk.Toplevel(self.root)
        help_page = HelpPage(help_window)  # Initialize HelpPage

    def show_credits(self):
        credits_window = tk.Toplevel(self.root)
        credits_window.title("Credits/About")
        credits_window.geometry(settings["window_size"])
        credits_window.configure(bg=settings["background_color"])
        lbl = tk.Label(credits_window, text="Credits/About page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def show_categories(self):
        categories_window = tk.Toplevel(self.root)
        categories_window.title("Categories")
        categories_window.geometry(settings["window_size"])
        categories_window.configure(bg=settings["background_color"])
        lbl = tk.Label(categories_window, text="Categories page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    home = HomePage(root)
    root.mainloop()
