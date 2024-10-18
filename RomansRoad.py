# Bible Trivia Quest - Romans Road
# Author: Scott Peterson
# Date: 10/16/24
# Description: This program is a trivia game that asks the user questions about the Romans Road to Salvation.
# The user is given a question and then given multiple choice answers. The user must select the correct answer.
# The user is given a score at the end of the game.

import tkinter as tk
import random
import json
from tkinter import simpledialog
import time

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Romans Road Trivia Game")
        self.load_questions()
        self.question_index = 0
        self.score = 0
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

        self.load_question()

    def load_questions(self):
        with open('romans_road.json', 'r') as file:
            self.questions = json.load(file)["Romans Road"]  # Load only Romans Road questions

    def load_question(self):
        self.answer_var.set("")
        self.feedback_label.config(text="")
        self.check_answer_button.config(state=tk.NORMAL)
        if self.question_index < len(self.questions):
            current_question = self.questions[self.question_index]
            self.question_label.config(text=current_question["question"])

            answers = [current_question["answer"]]
            while len(answers) < 4:
                wrong_answer = random.choice([q["answer"] for q in self.questions])
                if wrong_answer not in answers:
                    answers.append(wrong_answer)
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
            self.feedback_label.config(text=f"Correct!\nThe game will advance to the next question momentarily.")
            self.score += current_question["weight"]  # Increment the score by the question's weight
            self.root.after(3000, self.next_question)  # Wait 3 seconds for a correct answer
        else:
            self.feedback_label.config(text=f"Incorrect! \nThe correct answer is: \n{correct_answer}")
            self.root.after(7000, self.next_question)  # Wait 7 seconds for an incorrect answer
        self.score_label.config(text=f"Score: {round(self.score, 2)}")
        self.check_answer_button.config(state=tk.DISABLED)  # Disable the check answer button

    def next_question(self):
        self.check_answer_button.config(state=tk.NORMAL)  # Enable the check answer button for the next question
        self.question_index += 1
        self.load_question()

    def show_leaderboard(self):
        total_time = round(time.time() - self.start_time, 2)
        self.question_label.config(text=f"Congratulations! \nYou've completed all the questions in this section.")
        for button in self.option_buttons:
            button.pack_forget()
        self.check_answer_button.pack_forget()
        self.feedback_label.config(text=f"Final Score: {round(self.score, 2)}\nTotal Time: {total_time} seconds")
        self.save_score(total_time)

        # Clear the content frame for the leaderboard
        for widget in self.content_frame.winfo_children():
            widget.pack_forget()

        # Load existing scores
        try:
            with open('leaderboard.json', 'r') as file:
                leaderboard = json.load(file)
        except FileNotFoundError:
            leaderboard = []

        # Display the leaderboard
        leaderboard_label = tk.Label(self.content_frame, text="Top Scores", font=("Arial", 16), bg='white', wraplength=950)
        leaderboard_label.pack(pady=10)

        for entry in leaderboard:
            entry_label = tk.Label(self.content_frame, text=f"{entry['name']}: {entry['score']} (Time: {entry.get('time', 'N/A')} seconds)", font=("Arial", 14), bg='white', wraplength=950)
            entry_label.pack()

        # Restart button
        restart_button = tk.Button(self.content_frame, text="Restart Game", command=self.restart_game, font=("Arial", 14))
        restart_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.content_frame, text="Exit Game", command=self.root.quit, font=("Arial", 14))
        exit_button.pack(pady=10)

    def save_score(self, total_time):
        # Load existing scores
        try:
            with open('leaderboard.json', 'r') as file:
                leaderboard = json.load(file)
        except FileNotFoundError:
            leaderboard = []

        # Get the player's name and score
        player_name = self.ask_player_name()
        leaderboard.append({'name': player_name, 'score': round(self.score, 2), 'time': total_time})

        # Sort the leaderboard by score in descending order and keep the top 10
        leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]

        # Save the updated leaderboard
        with open('leaderboard.json', 'w') as file:
            json.dump(leaderboard, file, indent=4)

    def ask_player_name(self):
        return simpledialog.askstring("Name", "Enter your name for the leaderboard:")

    def restart_game(self):
        self.root.destroy()
        self.__init__(tk.Tk())

# Create the main window
root = tk.Tk()
game = TriviaGame(root)
root.mainloop()
