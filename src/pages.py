import tkinter as tk
from utilities import load_settings

# Load settings from settings.json
settings = load_settings("config/settings.json")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=settings["background_color"])

        welcome_label = tk.Label(self, text=settings["home_text"], font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        welcome_label.pack()

        text2_label = tk.Label(self, text="Prepared 4 \u221e - Home - ", wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        text2_label.pack(pady=10)

        psalm_label = tk.Label(self, text="                 Psalm 119:11\n I have hidden your word in my heart, that I might not sin against you. (NLT)", justify="left", wraplength=950, font=("Arial_Black", 18), bg=settings["background_color"], fg="gold")
        psalm_label.pack(pady=10)

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
        self.create_button(row1, "Help/Tutorial", lambda: controller.show_frame("HelpPage"), "#5e0e89", "#b654e9")

        # Second row of buttons
        row2 = tk.Frame(button_frame, bg=settings["background_color"])
        row2.pack(pady=15)

        self.create_button(row2, "Credits/About", self.show_credits, "#3c4056", "#c4cca6")
        self.create_button(row2, "Categories", self.show_categories, "#007ba7", "#00bfff")
        self.create_button(row2, "Exit", self.exit_app, "#8e0000", "#ff1c1c")

    def create_button(self, parent, text, command, bg, active_color):
        button = tk.Button(parent, text=text, command=command, bg=bg, fg="white", activebackground=active_color, activeforeground="black")
        button.pack(side=tk.LEFT, padx=10)

    def start_game(self):
        self.controller.root.destroy()
        game_window = tk.Tk()
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

class HelpPage(tk.Frame):
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
        button_frame.pack(pady=20, padx=20)

        self.create_help_button(button_frame, "Game Objective", self.show_game_objective, "#1c9431", "#16dc4c")
        self.create_help_button(button_frame, "Group Play", self.show_group_play, "#007ba7", "#00bfff")
        self.create_help_button(button_frame, "Scoring", self.show_scoring, "#c09601", "#f6c909")
        self.create_help_button(button_frame, "Difficulty Levels", self.show_difficulty_levels, "#6c5400", "#ff8c00")

        home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame("HomePage"), bg="#3c4056", fg="white", activebackground="#00bfff", activeforeground="black")
        home_button.pack(pady=20)

    def create_help_button(self, parent, text, command, bg, active_color):
        button = tk.Button(parent, text=text, command=command, bg=bg, fg="white", activebackground=active_color, activeforeground="black")
        button.pack(side=tk.LEFT, padx=20)

    def show_game_objective(self):
        self.show_detail_window("Game Objective", "Objective: Answer trivia questions to score points.\n\nBible Verse: Philippians 3:14\n'I press on toward the goal to win the prize for which God has called me heavenward in Christ Jesus.' (NIV)")

    def show_group_play(self):
        self.show_detail_window("Group Play", "Group Play: Connect to the local network for group play.\n\nBible Verse: Matthew 18:20\n'For where two or three gather in my name, there am I with them.' (NIV)")

    def show_scoring(self):
        self.show_detail_window("Scoring", "Scoring: Points are awarded for correct answers.\n\nBible Verse: Romans 6:23\n'For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.' (NIV)")

    def show_difficulty_levels(self):
        self.show_detail_window("Difficulty Levels", "Difficulty Levels: Select from different difficulty levels.\n\nBible Verse: James 1:2\n'Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds.' (NIV)")

    def show_detail_window(self, title, content):
        detail_window = tk.Toplevel(self)
        detail_window.title(title)
        detail_window.geometry("600x400")
        detail_window.configure(bg=settings["background_color"])

        detail_label = tk.Label(detail_window, text=content, wraplength=550, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="white")
        detail_label.pack(pady=20, padx=20)
