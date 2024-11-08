import tkinter as tk
import json
import sys
sys.path.append('/home/pi/Prepared4Eternity/src')
from welcome_page import WelcomePage
from home_page import HomePage
from game_logic import TriviaGame  # Ensure TriviaGame is imported correctly
from leaderboard import LeaderboardPage

def load_settings(settings_path):
    with open(settings_path, 'r') as file:
        settings = json.load(file)
    return settings

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Load settings
        settings_path = 'config/settings.json'
        self.settings = load_settings(settings_path)
        
        # Set window geometry from settings
        self.geometry(self.settings["window_size"])
        if self.settings.get("fullscreen"):
            self.attributes('-fullscreen', True)

        # Initialize container to hold all frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomePage, HomePage, LeaderboardPage, TriviaGame):  # Add all your page classes here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
