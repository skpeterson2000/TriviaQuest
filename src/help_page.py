import tkinter as tk
from utilities import load_settings
from home import HomePage  # Import HomePage to navigate back to home

# Load settings from settings.json
settings = load_settings("config/settings.json")

class HelpPage:
    def __init__(self, root):
        self.root = root
        self.root.title(settings["title"] + " - Help/Tutorial")
        self.root.geometry(settings["window_size"])
        self.root.configure(bg=settings["background_color"])

        help_label = tk.Label(root, text="Help/Tutorial", font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        help_label.pack(pady=20)

        # Instructions and Bible verse area
        instructions_text = (
            "Single Player Instructions:\n\n"
            "1. Select a category to begin.\n"
            "2. Answer the trivia questions to the best of your ability.\n"
            "3. Use the provided timer to challenge yourself.\n"
            "4. Your score will be calculated based on correct answers and speed.\n"
            "\nBible Verse:\nPhilippians 4:13\n'I can do all this through him who gives me strength.' (NIV)"
        )

        instructions_label = tk.Label(root, text=instructions_text, wraplength=900, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="white")
        instructions_label.pack(pady=20, padx=20)

        # Frame for buttons
        button_frame = tk.Frame(root, bg=settings["background_color"])
        button_frame.pack(pady=20, padx=20)

        # Buttons to open pop-up windows with themed colors, centered within the frame
        self.create_help_button(button_frame, "Game Objective", self.show_game_objective, bg="#1c9431", active_color="#16dc4c")
        self.create_help_button(button_frame, "Group Play", self.show_group_play, bg="#007ba7", active_color="#00bfff")
        self.create_help_button(button_frame, "Scoring", self.show_scoring, bg="#c09601", active_color="#f6c909")
        self.create_help_button(button_frame, "Difficulty Levels", self.show_difficulty_levels, bg="#6c5400", active_color="#ff8c00")

        # Home Button to navigate back to home page, centered within the frame
        home_button = tk.Button(root, text="Home", command=self.go_home, bg="#3c4056", fg="white", activebackground="#00bfff", activeforeground="black")
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
        detail_window = tk.Toplevel(self.root)
        detail_window.title(title)
        detail_window.geometry("600x400")
        detail_window.configure(bg=settings["background_color"])

        detail_label = tk.Label(detail_window, text=content, wraplength=550, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="white")
        detail_label.pack(pady=20, padx=20)

    def go_home(self):
        self.root.destroy()
        home_window = tk.Tk()
        home = HomePage(home_window)
        home_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    help_page = HelpPage(root)
    root.mainloop()
