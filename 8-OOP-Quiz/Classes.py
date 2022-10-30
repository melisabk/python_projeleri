


class Questions:
    def __init__(self, question, cohices, answer):
        self.question = question
        self.choices = cohices
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.index = 0
    
    def getQuestion(self):
        return self.questions[self.index]


    def increase_score (self):
        self.score += 100

    def showQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.index+1 }: {question.questions}")
        

        for i in question.choices:
            print("***" + i)



        answer = input("Cevabınızı giriniz: ")
        if question.check_answer(answer):
            print("tebrikler, doğru bildiniz :)")
            self.increase_score()
        else:
            print(f"üzgünüm, yanlış cevap verdiniz. Doğru cevap: {question.answer}")
        self.index += 1


        if len(self.questions) != self.index:
            self.showQuestion()
        else:
            print("tebrikler, quizi tamamladınız! Toplam puanınız: ", self.score)


