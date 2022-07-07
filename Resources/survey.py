class AnonymousSurvey:
    """Collect answers to survey questions"""

    def __init__(self, question):
        """store a question, prepare to store an answer"""
        self.question = question
        self.responces = []

    def show_question(self):
        """Show survey question"""
        print(self.question)

    def store_responce(self, responce):
        """store a single responce"""
        self.responces.append(new_responce)

    def show_result(self):
        """show all responces"""
        print("Survey Results:")
        for responce in responces:
            print(f" -{responce}")
