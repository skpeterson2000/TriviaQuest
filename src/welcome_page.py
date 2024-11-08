import tkinter as tk
import json
from utilities import load_settings

# Load settings from settings.json
settings = load_settings("config/settings.json")

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=settings["background_color"])

        welcome_label = tk.Label(self, text="Welcome to 'Prepared 4 ∞'", font=("Arial_Black", 24), bg=settings["background_color"], fg="gold")
        welcome_label.pack()

        welcome_text = (
            "This is a game designed to improve Biblical knowledge and sourcing proficiency while refining individual evangelism techniques and increasing intimacy with God and His Word."
        )
        welcome_text_label = tk.Label(self, text=welcome_text, wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        welcome_text_label.pack(pady=10)

        psalm_label = tk.Label(self, text="Psalm 119:11\n I have hidden your word in my heart, that I might not sin against you. (NLT)", justify="left", wraplength=950, font=("Arial_Black", 18), bg=settings["background_color"], fg="gold")
        psalm_label.pack(pady=10)

        additional_paragraph = (
            "The game is intended to be played in a group setting over a local network, but can also be played solitaire. Details on how to play, how to set up the game for a group setting can be found by clicking the Help/Tutorial section below."
        )
        additional_paragraph_label = tk.Label(self, text=additional_paragraph, wraplength=950, justify="left", font=("Arial", 14), bg=settings["background_color"], fg="gold")
        additional_paragraph_label.pack(pady=10, padx=20)

        proceed_button = tk.Button(self, text="Proceed to Game", command=self.proceed_to_game, bg="#107b21", fg="white", activebackground="#06e301", activeforeground="black")
        proceed_button.pack(pady=20)

    def proceed_to_game(self):
        self.controller.show_frame("HomePage")

def create_welcome_page():
    root = tk.Tk()
    welcome_page = WelcomePage(root, controller=None)
    welcome_page.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    create_welcome_page()
