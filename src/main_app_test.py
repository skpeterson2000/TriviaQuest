import tkinter as tk
import random
from utilities import load_settings

# Load settings from settings.json
settings = load_settings("config/settings.json")

# Scrolling source file data
psalm_119_11_versions = [
    {"translation": "King James Version (KJV)", "text": "Thy word have I hid in mine heart, that I might not sin against thee."},
    {"translation": "New International Version (NIV)", "text": "I have hidden your word in my heart that I might not sin against you."},
    {"translation": "English Standard Version (ESV)", "text": "I have stored up your word in my heart, that I might not sin against you."},
    {"translation": "New Living Translation (NLT)", "text": "I have hidden your word in my heart, that I might not sin against you."},
    {"translation": "New King James Version (NKJV)", "text": "Your word I have hidden in my heart, That I might not sin against You."},
    {"translation": "Holman Christian Standard Bible (HCSB)", "text": "I have treasured Your word in my heart so that I may not sin against You."},
    {"translation": "The Message (MSG)", "text": "I’ve banked your promises in the vault of my heart so I won’t sin myself bankrupt."}
]

class HomePageTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=settings["background_color"])

        welcome_label = tk.Label(self, text=settings["home_text"], font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        welcome_label.pack()

        text2_label = tk.Label(self, text="Prepared 4 \u221e - Home - ", wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        text2_label.pack(pady=10)

        self.psalm_label = tk.Label(self, text="", justify="left", wraplength=950, font=("Arial_Black", 18), bg=settings["background_color"], fg="gold")
        self.psalm_label.pack(pady=10)

        self.scroll_psalm_119_11_versions()

        text3_label = tk.Label(self, text="This game is intended to be played in a group setting over a local network, but can also be played solitaire. Details on how to play, how to set up the game for a group setting can be found by clicking the Help/Tutorial section below.", wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        text3_label.pack(pady=10)

        intro_text = tk.Label(self, text=settings["intro_text"], font=("Arial", 14), bg=settings["background_color"], fg="gold")
        intro_text.pack(pady=10)

        button_frame = tk.Frame(self, bg=settings["background_color"])
        button_frame.pack(pady=15, expand=True)

        # First row of buttons
        row1 = tk.Frame(button_frame, bg=settings["background_color"])
        row1.pack(pady=5)

        self.create_button(row1, "Start Game", self.start_game, "#107b21", "#06e301")
        self.create_button(row1, "Leaderboard", self.show_leaderboard, "#817808", "#f6c909")
        self.create_button(row1, "Settings", self.open_settings, "#6c5400", "#ff8c00")
        self.create_button(row1, "Help/Tutorial", lambda: controller.show_frame("HelpPageTest"), "#5e0e89", "#b654e9")

        # Second row of buttons
        row2 = tk.Frame(button_frame, bg=settings["background_color"])
        row2.pack(pady=15)

        self.create_button(row2, "Credits/About", self.show_credits, "#3c4056", "#c4cca6")
        self.create_button(row2, "Categories", self.show_categories, "#007ba7", "#00bfff")
        self.create_button(row2, "Exit", self.exit_app, "#8e0000", "#ff1c1c")

    def create_button(self, parent, text, command, bg, active_color):
        button = tk.Button(parent, text=text, command=command, bg=bg, fg="white", activebackground=active_color, activeforeground="black")
        button.pack(side=tk.LEFT, padx=10)

    def trigger_scroll(self):
        self.scroll_psalm_119_11_versions()
        self.after(52000, self.scroll_psalm_119_11_versions)

    def scroll_psalm_119_11_versions(self):
        version = random.choice(psalm_119_11_versions)
        self.psalm_label.config(text=f"{version['translation']}: {version['text']}")

    def start_game(self):
        self.controller.root.destroy()
        game_window = tk.Tk()
        from game_logic import TriviaGame  # Add this import statement at the top of the file if TriviaGame is defined in trivia_game.py
        game = TriviaGame(game_window)
        game_window.mainloop()

    def show_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.controller.root)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry(settings["window_size"])
        leaderboard_window.configure(bg=settings["background_color"])
        lbl = tk.Label(leaderboard_window, text="Leaderboard coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def open_settings(self):
        settings_window = tk.Toplevel(self.controller.root)
        settings_window.title("Settings")
        settings_window.geometry(settings["window_size"])
        settings_window.configure(bg=settings["background_color"])
        lbl = tk.Label(settings_window, text="Settings page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def show_credits(self):
        credits_window = tk.Toplevel(self.controller.root)
        credits_window.title("Credits/About")
        credits_window.geometry(settings["window_size"])
        credits_window.configure(bg=settings["background_color"])
        lbl = tk.Label(credits_window, text="Credits/About page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def show_categories(self):
        categories_window = tk.Toplevel(self.controller.root)
        categories_window.title("Categories")
        categories_window.geometry(settings["window_size"])
        categories_window.configure(bg=settings["background_color"])
        lbl = tk.Label(categories_window, text="Categories page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def exit_app(self):
        self.controller.root.destroy()

class HelpPageTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=settings["background_color"])

        help_label = tk.Label(self, text="Help/Tutorial", font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        help_label.pack(pady=20)

        instructions_text = (
            "Single Player Instructions:\n\n"
            "1. Select a category to begin.\n"
            "2. Answer the trivia questions to the best of your ability.\n"
            "3. Use the provided timer to challenge yourself.\n"
            "4. Your score will be calculated based on correct answers and speed.\n"
            "\nBible Verse:\nPhilippians 4:13\n'I can do all this through him who gives me strength.' (NIV)"
        )

        instructions_label = tk.Label(self, text=instructions_text, wraplength=900, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="white")
        instructions_label.pack(pady=20, padx=20)

        button_frame = tk.Frame(self, bg=settings["background_color"])
        button_frame.pack()

        