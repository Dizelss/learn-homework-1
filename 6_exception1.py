"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():

    base_ask_answer = {
        "Что делаешь?": "Программирую",
        "Как себя чувствуешь?": "Отлично",
        "Как дела?": "Отлично",
        "Хочешь поиграть?": "Давай!"
    }

    def ask_user_dict():
        while True:
            try:
                question = input("Введите Ваш вопрос: ")
                if question == "Хорошо":
                    print(f"Прогарамма завершила свою работу после ввода Вами слова {question}")
                    break
                else:
                    get_answer(question)
            except KeyboardInterrupt:
                print("Пока!")
                break

    # Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соответствующий ответ.
    def get_answer(question):
        if question in base_ask_answer:
            print(f"Ответ подобран из базы данных: {base_ask_answer[question]}")
        else:
            print(f"К сожалению, мне пока не известен ответ на Ваш вопрос {question}")

    ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
