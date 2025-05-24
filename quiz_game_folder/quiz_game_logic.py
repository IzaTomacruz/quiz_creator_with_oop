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

    def load_next_question(self):
        if len(self.used_questions) == 10:
            self.quiz_screen = False
            self.score_screen = True
        else:
            while True:
                next_q = random.choice(self.questions)
                if next_q not in self.used_questions:
                    self.current_question = next_q
                    self.used_questions.append(next_q)
                    break

    def reset_game(self):
        self.used_questions = []
        self.score = 0
        self.feedback_text = ""
        self.next_question = False
        self.current_question = None

    def back_home(self):
        self.reset_game()
        self.home_screen = True
        self.score_screen = False

    def play_again(self):
        self.used_questions = []
        self.score = 0
        self.feedback_text = ""
        self.next_question = False
        self.score_screen = False
        self.quiz_screen = True
        self.current_question = random.choice(self.questions)
        self.used_questions.append(self.current_question)

    def another_question(self):
        self.feedback_text = ""
        self.next_question = False
        self.load_next_question()

    def correct(self):
        self.feedback_text = "Correct!"
        self.score += 1

    def wrong(self):
        correct_key = self.current_question["answer"]
        self.feedback_text = f"Incorrect! Correct answer is: {correct_key}"

    # The Main loop of the game
    def run(self):
        while self.running:
            if self.home_screen:
                self.visual.draw_home_screen()
            elif self.quiz_screen:
                self.visual.draw_quiz_screen(self.current_question, self.feedback_text)
            elif self.score_screen:
                self.visual.draw_score_screen(self.score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_screen:
                        if self.visual.start_button.collidepoint(event.pos):
                            self.start_quiz()
                        elif self.visual.exit_button.collidepoint(event.pos):
                            self.running = False

                    elif self.score_screen:
                        if self.visual.play_again_button.collidepoint(event.pos):
                            self.play_again()
                        elif self.visual.back_menu_button.collidepoint(event.pos):
                            self.back_home()

                    elif self.quiz_screen:
                        if self.next_question:
                            self.another_question()
                        else:
                            for key, rect in self.visual.choice_buttons.items():
                                if rect.collidepoint(event.pos):
                                    if key == self.current_question["answer"]:
                                        self.correct()
                                    else:
                                        self.wrong()
                                    self.next_question = True
                                    break


            pygame.display.flip()
        pygame.quit()