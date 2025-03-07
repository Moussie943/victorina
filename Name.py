print("Это викторина на знание самого ужасного класса в школе (нашего). Ответь на вопросы и узнай, насколько хорошо ты разбираешься в 7А!")
question1 = 'Кто в классе самый шпала? '
question2 = 'кто самые ноготочки? '
question3 = "кто спортсменКА? "
question4 = "кто изношенный метал? "
question5 = "кто самый лентяй? "
answer1 = input(question1)
answer2 = input(question2)
answer3 = input(question3)
answer4 = input(question4)
answer5 = input(question5)
true_answer1 = "Корнеев"
true_answer2 = "Лера"
true_answer3 = "Миладзе"
true_answer4 = "Ржавый"
true_answer5 = "хз"
record = 0
if answer1 == true_answer1:
    record = record + 1
if answer2 == true_answer2:
    record = record + 1
if answer3 == true_answer3:
    record = record + 1
if answer4 == true_answer4:
    record = record + 1
if answer5 == true_answer5:
    record = record + 1
print(record)
