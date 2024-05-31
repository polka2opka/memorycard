from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint



class Question():
    def __init__(self, question, right_answer, wr_ans1, wr_ans2, wr_ans3):
        self.question = question
        self.answer = right_answer
        self.answer = wr_ans1
        self.answer = wr_ans2
        self.answer = wr_ans3




app = QApplication([])

window = QWidget()
window.setWindowTitle('memory Card')

window.score = 0
window.total = 0

questions=[]
questions.append(
    Question("Какой национальности не существует?", "Энцы", "Смурфы", "Чулымцы", "Алеуты")
)

questions.append(
    Question("Как называется тонкая но длинная страна?", " Республика Чили", "Республика Казахстан", "Республика Молдова", "Республика Чукотка")
)

questions.append(
    Question("Какого цвета черный цвет", "черный", "белый", "серый", "бермудовый")
)




question = QLabel('Какой национальности не существует?')
btn_Ok = QPushButton('Ответить')

layout_1 = QVBoxLayout()
layout_1.addWidget(question, alignment=Qt.AlignCenter)

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
line3.addWidget(btn_Ok, alignment=Qt.AlignCenter)

layout_1.addLayout(line1)
layout_1.addLayout(line2)
layout_1.addLayout(line3)

ansGroupBox = QGroupBox('Результаты')
lb_result = QLabel('Правильно или нет')
lb_correct = QLabel('Ответ будет тут')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)

ansGroupBox.setLayout(layout_res)

#line2 = QHBoxLayout()
#layout_1.addLayout(line2)
#line2.addWidget(ansGroupBox, alignment=Qt.AlignCenter)

def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    btn_Ok.setText('Следующий вопрос')


def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    btn_Ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question_text, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    question.setText(question_text)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:' , window.total, '/n-Правильных ответов:', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
def next_question():
    cur = randint(0, len(questions) - 1)
    q = questions[cur]
    ask(q)

#def test():
    #if 'Ответить' == btn_Ok.text():
        #show_result()
    #else:
        #show_question()

window.setLayout(layout_1)
ask('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
btn_Ok.clicked.connect(check_answer)
window.show()
app.exec()