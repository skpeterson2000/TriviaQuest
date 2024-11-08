import tkinter as tk
import random
import json
from utilities import load_settings

# Load Proverbs versions from JSON file
proverbs_versions_path = "/home/pi/Prepared4Eternity/data/proverbs_27_17_versions.json"
with open(proverbs_versions_path, "r") as file:
    proverbs_27_17_versions = json.load(file)

# Load leaderboard from JSON file
leaderboard_path = "/home/pi/Prepared4Eternity/data/leaderboard.json"
with open(leaderboard_path, "r") as file:
    leaderboard_data = json.load(file)

def sort_by_score_and_time(players):
    return sorted(players, key=lambda x: (-x['score'], x['time']))

class LeaderboardPage:
    def __init__(self, root, settings):
        self.root = root
        self.settings = settings

    def show_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Prepared 4 ∞ Hall of Fame")
        leaderboard_window.geometry(self.settings["window_size"])
        leaderboard_window.configure(bg=self.settings["background_color"])

        banner_label = tk.Label(leaderboard_window, text="Prepared 4 ∞ Hall of Fame", font=("Arial_Black", 24), bg=self.settings["background_color"], fg="gold")
        banner_label.grid(row=0, column=0, columnspan=12, pady=(10, 20))

        self.proverbs_label = tk.Label(leaderboard_window, text="", justify="left", wraplength=950, font=("Arial_Black", 20), bg=self.settings["background_color"], fg="#ebeb71")
        self.proverbs_label.grid(row=1, column=0, columnspan=12, pady=(10, 20))

        self.scroll_proverbs_27_17_versions(leaderboard_window)

        sorted_players = sort_by_score_and_time(leaderboard_data)
        if not sorted_players:
            no_data_label = tk.Label(leaderboard_window, text="No data available", font=("Arial", 16), bg=self.settings["background_color"], fg="white")
            no_data_label.grid(row=2, column=0, columnspan=12)
            return

        leaderboard_label = tk.Label(leaderboard_window, text="Leaderboard", font=("Arial_Black", 18), bg=self.settings["background_color"], fg="gold")
        leaderboard_label.grid(row=2, column=0, columnspan=6, pady=(10, 20))

        notable_label = tk.Label(leaderboard_window, text="Notable Mention", font=("Arial_Black", 18), bg=self.settings["background_color"], fg="silver")
        notable_label.grid(row=2, column=6, columnspan=6, pady=(10, 20))

        name_header = tk.Label(leaderboard_window, text="Name", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="gold")
        score_header = tk.Label(leaderboard_window, text="Score", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="gold")
        time_header = tk.Label(leaderboard_window, text="Time", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="gold")

        name_header.grid(row=3, column=0, padx=5)
        score_header.grid(row=3, column=1, padx=5)
        time_header.grid(row=3, column=2, padx=5)

        notable_name_header = tk.Label(leaderboard_window, text="Name", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="silver")
        notable_score_header = tk.Label(leaderboard_window, text="Score", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="silver")
        notable_time_header = tk.Label(leaderboard_window, text="Time", font=("Arial", 14, "bold"), bg=self.settings["background_color"], fg="silver")

        notable_name_header.grid(row=3, column=6, padx=5)
        notable_score_header.grid(row=3, column=7, padx=5)
        notable_time_header.grid(row=3, column=8, padx=5)

        for index, player in enumerate(sorted_players[:5], start=4):
            player_name = tk.Label(leaderboard_window, text=player['name'], bg=self.settings["background_color"], fg="white", font=("Arial", 14))
            player_score = tk.Label(leaderboard_window, text=player['score'], bg=self.settings["background_color"], fg="white", font=("Arial", 14))
            player_time = tk.Label(leaderboard_window, text=f"{player['time']} seconds", bg=self.settings["background_color"], fg="white", font=("Arial", 14))

            player_name.grid(row=index, column=0, padx=5)
            player_score.grid(row=index, column=1, padx=5)
            player_time.grid(row=index, column=2, padx=5)

        for index, player in enumerate(sorted_players[5:12], start=4):
            player_name = tk.Label(leaderboard_window, text=player['name'], bg=self.settings["background_color"], fg="white", font=("Arial", 14))
            player_score = tk.Label(leaderboard_window, text=player['score'], bg=self.settings["background_color"], fg="white", font=("Arial", 14))
            player_time = tk.Label(leaderboard_window, text=f"{player['time']} seconds", bg=self.settings["background_color"], fg="white", font=("Arial", 14))

            player_name.grid(row=index, column=6, padx=5)
            player_score.grid(row=index, column=7, padx=5)
            player_time.grid(row=index, column=8, padx=5)

    def scroll_proverbs_27_17_versions(self, leaderboard_window):
        version = random.choice(proverbs_27_17_versions)
        display_text = f"Proverbs 27:17 {version['text']}\t\t{version['translation']}"
        self.proverbs_label.config(text=display_text)
        leaderboard_window.after(52000, lambda: self.scroll_proverbs_27_17_versions(leaderboard_window))
