import json 

class QuizQuestion:
    # initialize
    def __init__(self):
        self.question = "" # Empty string for question
        self.choices = {} # Dictionary for choices 
        self.answer = "" # Empty string that only requires A, B, C, or D
        self.quiz_data = []

    def input_question(self): # Asks to input question and choices
        self.question = input("Enter a question: ")
        self.choices["A"] = input("Enter answer for A: ")
        self.choices["B"] = input("Enter answer for B: ")
        self.choices["C"] = input("Enter answer for C: ")
        self.choices["D"] = input("Enter answer for D: ")

    def input_answer(self):
        while True:
            answer = input("Enter the correct answer (A, B, C, D): ").upper()
            if answer in ["A", "B", "C", "D"]:
                self.answer = answer
                break
            print("Invalid input, please type A, B, C, or D only.")
            
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }
    
    
