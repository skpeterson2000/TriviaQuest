import tkinter as tk
import random

# Define the questions and answers
questions = [
    ("What is our universal condition according to Romans 3:23?", "For all have sinned and fall short of the glory of God."),
    ("What is the consequence of sin mentioned in Romans 6:23?", "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord."),
    ("How does God's love manifest according to Romans 5:8?", "But God demonstrates His own love for us in this: While we were still sinners, Christ died for us."),
    ("What does Romans 10:9 say about confessing Jesus as Lord?", "If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved."),
    ("What does Romans 10:13 say about calling on the name of the Lord?", "Everyone who calls on the name of the Lord will be saved."),
    ("According to Romans 5:1, what do we gain through faith?", "Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ."),
    ("What does Romans 8:1 assure believers?", "Therefore, there is now no condemnation for those who are in Christ Jesus."),
    ("How does Romans 8:38-39 describe God's love?", "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord."),
    ("What is the promise in Romans 8:28?", "And we know that in all things God works for the good of those who love him, who have been called according to his purpose."),
    ("What is the hope mentioned in Romans 15:13?", "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit."),
    ("According to Romans 12:1, how should believers live?", "Therefore, I urge you, brothers and sisters, in view of God's mercy, to offer your bodies as a living sacrifice, holy and pleasing to God—this is your true and proper worship."),
    ("What guidance does Romans 12:2 give for transformation?", "Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God's will is—his good, pleasing and perfect will.")
]

class TriviaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bible Trivia Game")
        self.root.geometry("1024x600")
        self.question_index = 0

        self.question_label = tk.Label(root, text=questions[self.question_index][0], wraplength=800, font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.option_buttons = [tk.Radiobutton(self.options_frame, text="", variable=self.answer_var, value="", wraplength=350, font=("Arial", 14)) for _ in range(4)]
        for button in self.option_buttons:
            button.pack(anchor='w', pady=5)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.show_answer_button = tk.Button(self.buttons_frame, text="Show Answer", command=self.show_answer, font=("Arial", 14))
        self.show_answer_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.buttons_frame, text="Next Question", command=self.next_question, font=("Arial", 14))
        self.next_button.grid(row=0, column=1, padx=5)

        self.answer_label = tk.Label(root, text="", font=("Arial", 14))
        self.answer_label.pack(pady=10)

        self.load_question()
        self.start_removal_timer()

    def load_question(self):
        self.answer_var.set("")
        correct_answer = questions[self.question_index][1]
        answers = [correct_answer]
        while len(answers) < 4:
            random_answer = random.choice([q[1] for q in questions])
            if random_answer not in answers:
                answers.append(random_answer)
        random.shuffle(answers)
        self.question_label.config(text=questions[self.question_index][0])
        for i, button in enumerate(self.option_buttons):
            button.config(text=answers[i], value=answers[i])

    def show_answer(self):
        selected_answer = self.answer_var.get()
        correct_answer = questions[self.question_index][1]
        if selected_answer == correct_answer:
            self.answer_label.config(text="Correct!")
        else:
            self.answer_label.config(text=f"Incorrect! The correct answer is: {correct_answer}")

    def next_question(self):
        self.question_index = (self.question_index + 1) % len(questions)
        self.answer_label.config(text="")
        self.load_question()
        self.start_removal_timer()

    def start_removal_timer(self):
        if hasattr(self, 'removal_timer'):
            self.root.after_cancel(self.removal_timer)  # Cancel any existing timer
        self.removal_timer = self.root.after(20000, self.remove_wrong_answer)  # Initial delay of 20 seconds before starting to remove answers

    def remove_wrong_answer(self):
        correct_answer = questions[self.question_index][1]
        wrong_answers = [button for button in self.option_buttons if button.cget("value") != correct_answer]
        if wrong_answers:
            button_to_remove = random.choice(wrong_answers)
            button_to_remove.config(text="", value="")
            if len(wrong_answers) > 1:
                self.removal_timer = self.root.after(5000, self.remove_wrong_answer)  # Continue removing an answer every 5 seconds

# Create the main window
root = tk.Tk()
game = TriviaGame(root)
root.mainloop()
