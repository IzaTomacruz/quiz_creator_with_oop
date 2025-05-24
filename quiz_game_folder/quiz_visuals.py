import pygame
import textwrap

class QuizVisual:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height   

        # colors
        self.color_white = (255, 255, 255)
        self.color_green = (36, 115, 57)
        self.color_yellowbrown = (213, 167, 40) 

        # backgrounds
        self.background_img = pygame.transform.scale(
            pygame.image.load("quiz_game_folder/graphics/background1.jpg"), (width, height))
        self.quiz_background = pygame.transform.scale(
            pygame.image.load("quiz_game_folder/graphics/background2.jpg"), (width, height))
        
        # fonts
        self.title_font = pygame.font.Font("quiz_game_folder/graphics/font.ttf", 34)
        self.button_font = pygame.font.Font("quiz_game_folder/graphics/font.ttf", 26)
        self.quiz_font = pygame.font.Font("quiz_game_folder/graphics/font.ttf", 13)

        #buttons
        self.start_button = pygame.Rect(300, 280, 200, 60)
        self.exit_button = pygame.Rect(300, 380, 200, 60)
        self.play_again_button = pygame.Rect(220, 280, 350, 60)
        self.back_menu_button = pygame.Rect(245, 380, 300, 60)

        self.choice_buttons = {
            "A": pygame.Rect(100, 180, 60, 60),
            "B": pygame.Rect(100, 260, 60, 60),
            "C": pygame.Rect(100, 340, 60, 60),
            "D": pygame.Rect(100, 420, 60, 60)
        }

    def draw_home_screen(self):
        self.screen.blit(self.background_img, (0, 0))
        title = self.title_font.render("Welcome to Quiz Game!", True, self.color_yellowbrown)
        title_rect = title.get_rect(center=(self.width // 2, 150))
        self.screen.blit(title, title_rect)

        pygame.draw.rect(self.screen, self.color_green, self.start_button)
        pygame.draw.rect(self.screen, self.color_green, self.exit_button)

        start_text = self.button_font.render("START", True, self.color_white)
        exit_text = self.button_font.render("EXIT", True, self.color_white)

        self.screen.blit(start_text, (self.start_button.x + 40, self.start_button.y + 17))
        self.screen.blit(exit_text, (self.exit_button.x + 48, self.exit_button.y + 17))

    def draw_quiz_screen(self, current_question, feedback_text):
        # question
        self.screen.blit(self.quiz_background, (0, 0))
        if current_question:
            question_text = current_question["question"]
            wrapped_lines = textwrap.wrap(question_text, width=45)  
            question_y = 100 

            for line in wrapped_lines:
                question = self.quiz_font.render(line, True, self.color_white)
                self.screen.blit(question, (100, question_y))
                question_y += 25
            # choices
            for key, rect in self.choice_buttons.items():
                pygame.draw.rect(self.screen, self.color_yellowbrown, rect)
                label = self.button_font.render(key, True, self.color_white)
                self.screen.blit(label, (rect.x + 17, rect.y + 17))

                choice_text = current_question["choices"][key]
                wrapped_choice_lines = textwrap.wrap(choice_text, width=40)
                choice_y = rect.y + 5

                for line in wrapped_choice_lines:
                    choice_line = self.quiz_font.render(line, True, self.color_white)
                    self.screen.blit(choice_line, (rect.x + 80, choice_y))  
                    choice_y += 24

        if feedback_text:
            feedback = self.quiz_font.render(feedback_text, True, self.color_white)
            self.screen.blit(feedback, (100, 500))

    def draw_score_screen(self, score):
        self.screen.blit(self.background_img, (0, 0))
        title = self.title_font.render(f"Your score is {score}/10", True, self.color_yellowbrown)
        self.screen.blit(title, title.get_rect(center=(self.width // 2, 150)))

        pygame.draw.rect(self.screen, self.color_green, self.play_again_button)
        pygame.draw.rect(self.screen, self.color_green, self.back_menu_button)

        again_text = self.button_font.render("PLAY AGAIN", True, self.color_white)
        menu_text = self.button_font.render("MAIN MENU", True, self.color_white)

        self.screen.blit(again_text, (self.play_again_button.x + 47, self.play_again_button.y + 17))
        self.screen.blit(menu_text, (self.back_menu_button.x + 37, self.back_menu_button.y + 17))