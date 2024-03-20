from survey import AnonymousSurvey

# define a question ,the craete a survey.
question = 'What language did you first to speak?'
my_survey = AnonymousSurvey(question)

# show question and store the answer
my_survey.show_question()
print("Enter 'q' to at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

# show the result of survey
print("\n Thank you to everyone who participated in the survey!")
my_survey.show_results()

