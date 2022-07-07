from survey import AnonymousSurvey
"""Define a question, and make a survey"""
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

"""show the question and store responces to the question"""
my_survey.show_question()
print("Enter q to quit")
while True:
    responce = input("Language: ")
    if responce == 'q':
        break
    my_survey.store_responce(responce)

"""Show results"""
print("Thank you for participating")
my_survey.show_result()
