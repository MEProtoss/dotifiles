class AnonymousSurvey:
    """Collect answers to anonymous survey questionnaires"""
    def __init__(self,question):
        """Store a question and prepare for storing an answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show survey questionnaires"""
        print(self.question)

    def store_response(self,new_response):
        """Store a single survey questionnaire"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the survey questionnaires collected"""
        print('Survey results:')
        for response in self.responses:
            print(f"-{response}")
