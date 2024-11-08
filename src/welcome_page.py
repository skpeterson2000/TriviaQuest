import tkinter as tk
import json

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="lightblue")

        welcome_label = tk.Label(self, text="Welcome to Prepared 4 Eternity!", font=("Arial_Black", 24), bg="lightblue", fg="gold")
        welcome_label.pack(pady=20)

        paragraph_text = (
            "Welcome to Prepared 4 Eternity! This game is designed to be both entertaining and educational, helping you to grow in your faith and knowledge. "
            "Please take your time to explore the various sections and complete the challenges ahead."
        )

        paragraph_label = tk.Label(self, text=paragraph_text, wraplength=900, justify="left", font=("Arial", 14), bg="lightblue", fg="white")
        paragraph_label.pack(pady=20, padx=20)

        start_button = tk.Button(self, text="Proceed to Game", command=self.check_token_and_proceed, bg="#1c9431", fg="white", activebackground="#16dc4c", activeforeground="black")
        start_button.pack(pady=20)

    def check_token_and_proceed(self):
        if self.check_token():
            self.controller.show_frame("HomePage")
        else:
            self.show_romans_road_warning()

    def check_token(self):
        try:
            with open("token.json", "r") as file:
                token = json.load(file)
            return token.get("completed_romans_road", False)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def show_romans_road_warning(self):
        warning_window = tk.Toplevel(self)
        warning_window.title("Complete Romans Road")
        warning_window.geometry("600x400")
        warning_window.configure(bg="lightblue")

        warning_label = tk.Label(warning_window, text="Please complete the first 5 questions of the Romans Road to continue.", font=("Arial_Black", 16), bg="lightblue", fg="red")
        warning_label.pack(pady=50)

        start_button = tk.Button(warning_window, text="Start Romans Road", command=self.complete_romans_road, bg="#1c9431", fg="white", activebackground="#16dc4c", activeforeground="black")
        start_button.pack(pady=20)

    def complete_romans_road(self):
        self.update_token()
        self.controller.show_frame("HomePage")

    def update_token(self):
        token = {"completed_romans_road": True}
        with open("token.json", "w") as file:
            json.dump(token, file)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x600")
    welcome_page = WelcomePage(parent=root, controller=None)
    welcome_page.pack(fill="both", expand=True)
    root.mainloop()
