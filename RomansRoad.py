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

# Define the questions, answers, and weights
questions = [
    ("What is our universal condition according to Romans 3:23?", "For all have sinned and fall short of the glory of God.", 10),
    ("What is the consequence of sin mentioned in Romans 6:23?", "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.", 10),
    ("How does God's love manifest according to Romans 5:8?", "But God demonstrates His own love for us in this: While we were still sinners, Christ died for us.", 10),
    ("What does Romans 10:9 say about confessing Jesus as Lord?", "If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved.", 10),
    ("What does Romans 10:13 say about calling on the name of the Lord?", "Everyone who calls on the name of the Lord will be saved.", 10),
    ("According to Romans 5:1, what do we gain through faith?", "Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ.", 10),
    ("What does Romans 8:1 assure believers?", "Therefore, there is now no condemnation for those who are in Christ Jesus.", 10),
    ("How does Romans 8:38-39 describe God's love?", "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.", 10),
    ("What is the promise in Romans 8:28?", "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.", 10),
    ("What is the hope mentioned in Romans 15:13?", "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.", 10),
    ("According to Romans 12:1, how should believers live?", "Therefore, I urge you, brothers and sisters, in view of God's mercy, to offer your bodies as a living sacrifice, holy and pleasing to God—this is your true and proper worship.", 10),
    ("What guidance does Romans 12:2 give for transformation?", "Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—his good, pleasing and perfect will.", 10.01)
]

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bible Trivia Game")
        self.questions = random.sample(questions, len(questions))  # Randomize the order of questions
        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=800, font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.option_buttons = [tk.Radiobutton(self.options_frame, text="", variable=self.answer_var, value="", wraplength=650, font=("Arial", 14)) for _ in range(4)]
        for button in self.option_buttons:
            button.pack(anchor='w', pady=5)

        self.check_answer_button = tk.Button(root, text="Check Answer", command=self.check_answer, font=("Arial", 14))
        self.check_answer_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.answer_var.set("")
        self.feedback_label.config(text="")
        self.check_answer_button.config(state=tk.NORMAL)
        if self.question_index < len(self.questions):
            current_question = self.questions[self.question_index]
            self.question_label.config(text=current_question[0])

            answers = [current_question[1]]
            while len(answers) < 4:
                wrong_answer = random.choice([q[1] for q in self.questions])
                if wrong_answer not in answers:
                    answers.append(wrong_answer)
            random.shuffle(answers)

            for i, button in enumerate(self.option_buttons):
                button.config(text=answers[i], value=answers[i])
        else:
            self.question_label.config(text="Congratulations! You've completed all the questions.")
            for button in self.option_buttons:
                button.pack_forget()
            self.check_answer_button.pack_forget()
            self.next_button.pack_forget()
            self.feedback_label.config(text=f"Final Score: {round(self.score, 2)}")
            self.save_score()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        current_question = self.questions[self.question_index]
        correct_answer = current_question[1]
        if selected_answer == correct_answer:
            self.feedback_label.config(text="Correct!")
            self.score += current_question[2]  # Increment the score by the question's weight
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", wraplength=650)
        self.score_label.config(text=f"Score: {round(self.score, 2)}")
        self.check_answer_button.config(state=tk.DISABLED)  # Disable the check answer button

    def next_question(self):
        self.question_index += 1
        self.load_question()

    def save_score(self):
        # Load existing scores
        try:
            with open('leaderboard.json', 'r') as file:
                leaderboard = json.load(file)
        except FileNotFoundError:
            leaderboard = []

        # Get the player's name and score
        player_name = self.ask_player_name()
        leaderboard.append({'name': player_name, 'score': round(self.score, 2)})

        # Sort the leaderboard by score in descending order and keep the top 10
        leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]

        # Save the updated leaderboard
        with open('leaderboard.json', 'w') as file:
            json.dump(leaderboard, file, indent=4)

    def ask_player_name(self):
        return simpledialog.askstring("Name", "Enter your name for the leaderboard:")

# Create the main window
root = tk.Tk()
game = TriviaGame(root)
root.mainloop()
