import tkinter as tk
import json

class LeaderboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='lightblue')

        title_label = tk.Label(self, text="Leaderboard", font=("Arial", 24), bg='lightblue')
        title_label.pack(pady=20)

        self.leaderboard_data = self.load_leaderboard_data()

        self.leaderboard_text = tk.Text(self, wrap="word", bg='lightblue', font=("Arial", 12))
        self.leaderboard_text.pack(expand=True, fill='both', padx=20, pady=20)

        self.display_leaderboard()

        back_button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)

    def load_leaderboard_data(self):
        with open('/home/pi/Prepared4Eternity/src/data/leaderboard.json', 'r') as file:
            return json.load(file)

    def display_leaderboard(self):
        self.leaderboard_text.delete(1.0, tk.END)
        for entry in self.leaderboard_data:
            self.leaderboard_text.insert(tk.END, f"Name: {entry['name']}, Score: {entry['score']}, Time: {entry['time']} seconds\n")
        self.leaderboard_text.config(state=tk.DISABLED)
