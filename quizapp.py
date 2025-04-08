import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        # Quiz questions, options, and correct answer indices
        self.quiz_data = [
            {
                "question": "Which data structure uses FIFO (First In First Out)?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "correct_answer": 1
            },
            {
                "question": "What does CPU stand for?",
                "options": ["Central Process Unit", "Computer Processing Unit", "Central Processing Unit", "Control Processing Unit"],
                "correct_answer": 2
            },
            {
                "question": "Which sorting algorithm is the fastest in average case?",
                "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"],
                "correct_answer": 2
            },
            {
                "question": "What is the time complexity of binary search?",
                "options": ["O(n)", "O(n log n)", "O(log n)", "O(1)"],
                "correct_answer": 2
            },
            {
                "question": "In OOP, what does 'inheritance' mean?",
                "options": ["Creating multiple instances", "Using the same function name", "Deriving a class from another", "Hiding data"],
                "correct_answer": 2
            },
            {
                "question": "Which of the following is a NoSQL database?",
                "options": ["MySQL", "MongoDB", "Oracle", "PostgreSQL"],
                "correct_answer": 1
            },
            {
                "question": "Which layer in OSI model is responsible for end-to-end communication?",
                "options": ["Data Link", "Transport", "Network", "Session"],
                "correct_answer": 1
            },
            {
                "question": "Which protocol is used to send emails?",
                "options": ["HTTP", "FTP", "SMTP", "POP3"],
                "correct_answer": 2
            },
            {
                "question": "Which of the following is not a programming language?",
                "options": ["Python", "Java", "HTML", "C++"],
                "correct_answer": 2
            },
            {
                "question": "Which keyword is used to create a function in Python?",
                "options": ["def", "function", "func", "define"],
                "correct_answer": 0
            }
        ]

        self.current_question_index = 0
        self.score = 0

        # Main application window
        self.window = tk.Tk()
        self.window.title("QUIZ APP WITH PYTHON")

        # Label to display the current question
        self.question_label = tk.Label(self.window, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        # Frame to contain all option buttons
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        # Creating 4 option buttons
        self.option_buttons = []
        for i in range(4):  # ✅ Only 4 options per question
            button = tk.Button(
                self.options_frame, text="", width=40,
                command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5)
            self.option_buttons.append(button)

        # Button to load the next question
        self.next_question_button = tk.Button(
            self.window, text="Next Question", width=30,
            command=self.next_question
        )
        self.next_question_button.pack(pady=10)

    def next_question(self):
        # Move to the next question
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            # Display score when quiz ends
            messagebox.showinfo("GAME OVER", "YOUR SCORE IS: " + str(self.score))
            self.window.quit()
        else:
            self.load_question()

    def check_answer(self, selected_option):
        # Check if selected option is correct
        question_data = self.quiz_data[self.current_question_index]
        answer = question_data['correct_answer']
        if selected_option == answer:
            self.score += 1
            messagebox.showinfo("CORRECT", "YOUR ANSWER IS CORRECT")
        else:
            messagebox.showinfo("INCORRECT", "YOUR ANSWER IS INCORRECT")

    def load_question(self):
        # Load the current question and its options
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        options = question_data['options']
        for i in range(4):  # ✅ Always only 4 options
            self.option_buttons[i].config(text=options[i])

    def start_quiz(self):
        # Start the quiz
        self.load_question()
        self.window.mainloop()

# Create and start the quiz app
quiz_app = QuizApp()
quiz_app.start_quiz()
