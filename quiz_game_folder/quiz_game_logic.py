import pygame
import json
import random
from quiz_visuals import QuizVisual

class QuizGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Quiz Game")

        with open("quiz_game_folder/questions.json") as f:
            self.questions = json.load(f)

        self.visual = QuizVisual(self.screen, self.width, self.height)

        self.home_screen = True
        self.quiz_screen = False
        self.score_screen = False
        self.running = True
        self.feedback_text = ""
        self.next_question = False
        self.used_questions = []
        self.score = 0
        self.current_question = None

    def start_quiz(self):
        self.home_screen = False
        self.quiz_screen = True
        self.current_question = random.choice(self.questions)
        self.used_questions.append(self.current_question)
