from quiz_creator import QuizQuestion, QuizCreator

print("WELCOME TO THE QUIZ CREATOR!\n")
print("Please write down your questions, choices, and answers below:\n")

create = QuizCreator()

while True:
    question = QuizQuestion()
    question.input_question()
    question.input_answer()

    if create.confirm_save():
        create.quiz_data.append(question.to_dict())
        print("Question saved")

    if not create.ask_continue():
        break

create.save() 
print("Thank you for using Quiz Creator")