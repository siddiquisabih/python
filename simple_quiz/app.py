import questionAnswer as qs


class App():

    startQuiz = input('want to start a quiz (y /n )')
    if startQuiz == 'y':
        question = qs.Question().ask_question()

    else:
        print('thank you get lost ')





