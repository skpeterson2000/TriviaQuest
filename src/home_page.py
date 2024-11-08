import tkinter as tk
import random
import json
from tkinter import font
from utilities import load_settings, create_button

# Add src to Python path for imports
import sys
sys.path.append('/home/pi/Prepared4Eternity/src')

from game_logic import TriviaGame
from help_page import open_help_page
from leaderboard import LeaderboardPage

# Load settings from the correct path
settings = load_settings("config/settings.json")

# Load Psalm versions from JSON file
psalm_versions_path = "/home/pi/Prepared4Eternity/src/data/psalm_119_11_versions.json"
with open(psalm_versions_path, "r") as file:
    psalm_119_11_versions = json.load(file)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=settings["background_color"])

        welcome_label = tk.Label(self, text=settings["home_banner"], font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        welcome_label.pack()

        text2_label = tk.Label(self, text=settings["home_text"], wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="#10b9fb")
        text2_label.pack(pady=10)

        self.psalm_label = tk.Label(self, text="", justify="left", wraplength=950, font=("Arial_Black", 20), bg=settings["background_color"], fg="#ebeb71")
        self.psalm_label.pack(pady=10)

        self.scroll_psalm_119_11_versions()

        text3_label = tk.Label(self, text=settings["invite_text"], font=("Arial", 14), wraplength=950, justify="left", bg=settings["background_color"], fg="#10b9fb")
        text3_label.pack(pady=10)

        intro_text = tk.Label(self, text=settings["vision_text"], font=("Arial", 16), bg=settings["background_color"], fg="#e44111")
        intro_text.pack(pady=10)

        button_frame = tk.Frame(self, bg=settings["background_color"])
        button_frame.pack(pady=15, expand=True)

        create_button(button_frame, "Start Game", self.start_game, "#107b21", "#06e301")
        create_button(button_frame, "Leaderboard", self.show_leaderboard, "#817808", "#f6c909")
        create_button(button_frame, "Settings", self.open_settings, "#6c5400", "#ff8c00")
        create_button(button_frame, "Help/Tutorial", self.open_help, "#5e0e89", "#b654e9")
        create_button(button_frame, "Credits/About", self.show_credits, "#3c4056", "#c4cca6")
        create_button(button_frame, "Categories", self.show_categories, "#007ba7", "#00bfff")
        create_button(button_frame, "Exit", self.exit_app, "#8e0000", "#ff1c1c")

    def scroll_psalm_119_11_versions(self):
        version = random.choice(psalm_119_11_versions)
        display_text = f"Psalm 119:11 {version['text']}\t\t{version['translation']}"
        self.psalm_label.config(text=display_text)
        self.after(52000, self.scroll_psalm_119_11_versions)

    def start_game(self):
        self.controller.show_frame("TriviaGame")

    def show_leaderboard(self):
        self.controller.show_frame("LeaderboardPage")

    def open_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.title("Settings")
        settings_window.geometry(settings["window_size"])
        settings_window.configure(bg=settings["background_color"])
        lbl = tk.Label(settings_window, text="Settings page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def open_help(self):
        open_help_page(self)

    def show_credits(self):
        credits_window = tk.Toplevel(self)
        credits_window.title("Credits/About")
        credits_window.geometry(settings["window_size"])
        credits_window.configure(bg=settings["background_color"])
        lbl = tk.Label(credits_window, text="Credits/About page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def show_categories(self):
        categories_window = tk.Toplevel(self)
        categories_window.title("Categories")
        categories_window.geometry(settings["window_size"])
        categories_window.configure(bg=settings["background_color"])
        lbl = tk.Label(categories_window, text="Categories page coming soon!", bg=settings["background_color"], fg="white", font=("Arial", 24))
        lbl.pack(pady=50)

    def exit_app(self):
        self.controller.quit()
