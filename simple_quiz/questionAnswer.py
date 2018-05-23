class Question ():

    def __init__(self):
        self.questions = [{'id': 1, 'question': 'How many meter in 1 kilometer? ', 'answer': '1000'},
                          {'id': 2, 'question': 'How many items in One dozen ? ', 'answer': '12'},
                          {'id': 3, 'question': 'what is your company Name ? ', 'answer': 'texpo'},
                          ]
        self.answer = []
        self.wrongAnswer = []

    def ask_question(self):
        for a in self.questions:
            ans = input ('Q' + str(a['id']) + ': ' + a['question'])
            if ans == a['answer']:
                self.answer.append (a['answer'])
            else:
                self.wrongAnswer.append (a['answer'])

        checkrec = input('\nDo You want to see your result (y/n) \n')
        if checkrec == 'y':
            self.calculateResult (self.answer, self.wrongAnswer)

    def calculateResult(self, ans, wrongans):
        lengthAns = len (ans)
        worngLen = len (wrongans)

        if lengthAns != 0:
            print ('\nYou Give ' + str (lengthAns) + " correct answer and " + str (worngLen) + " incorrect answer")
        else:
            print ('\nyou Give ' + str (worngLen) + " incorrect answer")
