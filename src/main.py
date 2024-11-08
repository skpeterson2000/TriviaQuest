import json
import tkinter as tk
from pages import HomePage, HelpPage  # Assume the WelcomePage is in the same module

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prepared 4 Eternity")
        self.root.geometry("1024x600")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # Create frames for HomePage and HelpPage
        for F in (HomePage, HelpPage):
            page_name = F.__name__
            frame = F(parent=self.root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Import and create the WelcomePage frame
        from welcome_page import WelcomePage
        welcome_frame = WelcomePage(parent=self.root, controller=self)
        self.frames["WelcomePage"] = welcome_frame
        welcome_frame.grid(row=0, column=0, sticky="nsew")

        # Show the WelcomePage initially
        self.show_frame("WelcomePage")

    def check_token(self):
        try:
            with open("token.json", "r") as file:
                token = json.load(file)
            return token.get("completed_romans_road", False)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
