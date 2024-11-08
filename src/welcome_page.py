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

        button_frame = tk.Frame(self, bg=settings["background_color"])
        button_frame.pack(pady=15)

        proceed_button = tk.Button(button_frame, text="Proceed to Game", command=self.proceed_to_game, bg="#107b21", fg="white", activebackground="#06e301", activeforeground="black")
        proceed_button.pack(side=tk.LEFT, padx=10)

        login_button = tk.Button(button_frame, text="Returning Player Login", command=self.open_login_popup, bg="#0074b7", fg="white", activebackground="#33b5e5", activeforeground="black")
        login_button.pack(side=tk.LEFT, padx=10)

        exit_button = tk.Button(button_frame, text="Exit Game", command=self.exit_game, bg="#8e0000", fg="white", activebackground="#ff1c1c", activeforeground="black")
        exit_button.pack(side=tk.LEFT, padx=10)

    def proceed_to_game(self):
        self.controller.show_frame("TriviaGame")

    def open_login_popup(self):
        login_popup = tk.Toplevel(self)
        login_popup.title("Returning Player Login")
        login_popup.geometry("300x200")
        login_popup.configure(bg=settings["background_color"])

        tk.Label(login_popup, text="Identity:", font=("Arial", 12), bg=settings["background_color"], fg="white").pack(pady=10)
        identity_entry = tk.Entry(login_popup)
        identity_entry.pack(pady=5)

        tk.Label(login_popup, text="Password:", font=("Arial", 12), bg=settings["background_color"], fg="white").pack(pady=10)
        password_entry = tk.Entry(login_popup, show="*")
        password_entry.pack(pady=5)

        button_frame = tk.Frame(login_popup, bg=settings["background_color"])
        button_frame.pack(pady=10)

        cancel_button = tk.Button(button_frame, text="Cancel", command=login_popup.destroy, bg="#8e0000", fg="white", activebackground="#ff1c1c", activeforeground="black")
        cancel_button.pack(side=tk.LEFT, padx=5)

        submit_button = tk.Button(button_frame, text="Submit", command=lambda: self.validate_login(identity_entry.get(), password_entry.get(), login_popup), bg="#107b21", fg="white", activebackground="#06e301", activeforeground="black")
        submit_button.pack(side=tk.LEFT, padx=5)

    def validate_login(self, identity, password, login_popup):
        print(f"Identity: {identity}, Password: {password}")
        login_popup.destroy()

    def exit_game(self):
        self.controller.quit()

def create_welcome_page():
    root = tk.Tk()
    root.geometry(settings["window_size"])
    if settings.get("fullscreen"):
        root.attributes('-fullscreen', True)
    welcome_page = WelcomePage(root, controller=None)
    welcome_page.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    create_welcome_page()
