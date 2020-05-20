"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        question = input("Как дела? ")
        if question == "Хорошо":
            print(f"Прогарамма завершила свою работу после ввода Вами слова {question}")
            break

    
if __name__ == "__main__":
    ask_user()
