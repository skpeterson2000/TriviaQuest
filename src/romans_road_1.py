import os
import tkinter as tk
import random
import json
from tkinter import simpledialog
import time
from leaderboard import LeaderboardPage

def load_settings(settings_path):
    with open(settings_path, 'r') as file:
        settings = json.load(file)
    return settings

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Prepared 4 ∞: Romans Road: Level 1")
        self.load_questions()
        self.question_index = 0
        self.score = 0
        self.tokens = 0
        self.start_time = time.time()

        # Frame for content
        self.content_frame = tk.Frame(root, bg='white')
        self.content_frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.question_label = tk.Label(self.content_frame, text="", wraplength=950, font=("Arial", 16), bg='white')
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.options_frame = tk.Frame(self.content_frame, bg='white')
        self.options_frame.pack(pady=10)

        self.option_buttons = [tk.Radiobutton(self.options_frame, text="", variable=self.answer_var, value="", wraplength=950, font=("Arial", 14), bg='white') for _ in range(4)]
        for button in self.option_buttons:
            button.pack(anchor='w', pady=5)

        self.check_answer_button = tk.Button(self.content_frame, text="Check Answer", command=self.check_answer, font=("Arial", 14))
        self.check_answer_button.pack(pady=10)

        self.feedback_label = tk.Label(self.content_frame, text="", wraplength=950, font=("Arial", 14), bg='white')
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(self.content_frame, text="Score: 0", wraplength=950, font=("Arial", 14), bg='white')
        self.score_label.pack(pady=10)

        self.exit_button = tk.Button(self.content_frame, text="Exit Game", command=self.root.quit, font=("Arial", 14))
        self.exit_button.pack(pady=10)

        # Load settings
        settings_path = '/home/pi/Prepared4Eternity/config/settings.json'
        settings = load_settings(settings_path)

        self.leaderboard = LeaderboardPage(self.root, settings)

        self.load_question()

    def load_questions(self):
        json_path = '/home/pi/Prepared4Eternity/src/data/romans_road_l1.json'
        print(f"Attempting to open JSON file at: {json_path}")
        with open(json_path, 'r') as file:
            self.questions = json.load(file)["questions"]

    def load_question(self):
        self.answer_var.set("")
        self.feedback_label.config(text="")
        self.check_answer_button.config(state=tk.NORMAL)
        if self.question_index < len(self.questions):
            current_question = self.questions[self.question_index]
            self.question_label.config(text=current_question["question"])

            all_answers = [q["answer"] for q in self.questions]
            all_answers = list(set(all_answers) - {current_question["answer"]})

            wrong_answers = random.sample(all_answers, 3)
            answers = [current_question["answer"]] + wrong_answers
            random.shuffle(answers)

            for i, button in enumerate(self.option_buttons):
                button.config(text=answers[i], value=answers[i])
        else:
            self.show_leaderboard()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        current_question = self.questions[self.question_index]
        correct_answer = current_question["answer"]
        if selected_answer == correct_answer:
            self.feedback_label.config(text="Excellent! The game will advance to the next question momentarily.")
            self.score += current_question["weight"]
            for button in self.option_buttons:
                if button.cget("value") == correct_answer:
                    button.config(bg="green", fg="white")
            self.root.after(3000, self.next_question)
        else:
            self.feedback_label.config(text=f"The correct answer is: {correct_answer}")
            for button in self.option_buttons:
                if button.cget("value") == correct_answer:
                    button.config(bg="green", fg="white")
                elif button.cget("value") == selected_answer:
                    button.config(bg="#ff5433")
            self.root.after(8000, self.next_question)
        self.score_label.config(text=f"Score: {round(self.score, 2)}")
        self.check_answer_button.config(state=tk.DISABLED)

    def next_question(self):
        self.check_answer_button.config(state=tk.NORMAL)
        for button in self.option_buttons:
            button.config(bg="white")
        self.question_index += 1
        self.load_question()

    def show_leaderboard(self):
        total_time = round(time.time() - self.start_time, 2)
        self.question_label.config(text="Congratulations! You've completed all the questions in this section.")
        for button in self.option_buttons:
            button.pack_forget()
        self.check_answer_button.pack_forget()
        self.feedback_label.config(text=f"Final Score: {round(self.score, 2)}\nTotal Time: {total_time} seconds")
        name = simpledialog.askstring("Name", "Please enter your name:")
        
        # Save the score to the leaderboard
        leaderboard_data = {
            "name": name,
            "score": round(self.score, 2),
            "time": total_time
        }
        with open('/home/pi/Prepared4Eternity/src/data/leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
        leaderboard.append(leaderboard_data)
        with open('/home/pi/Prepared4Eternity/src/data/leaderboard.json', 'w') as file:
            json.dump(leaderboard, file)
        
        # Check for token award
        if self.score >= 5:
            self.tokens += 1
            print(f"Congratulations! You've earned a token. Total tokens: {self.tokens}")

        # Display the updated leaderboard
        self.leaderboard.show_leaderboard()

        # Restart button
        restart_button = tk.Button(self.content_frame, text="Restart Game", command=self.restart_game, font=("Arial", 14))
        restart_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.content_frame, text="Exit Game", command=self.root.quit, font=("Arial", 14))
        exit_button.pack(pady=10)

    def restart_game(self):
        self.question_index = 0
        self.score = 0
        self.start_time = time.time()
        self.load_question()

def create_game():
    root = tk.Tk()
    game = TriviaGame(root)
    root.mainloop()

if __name__ == "__main__":
    create_game()
