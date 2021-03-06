"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def what_to_do(age):
    if 0 < age <= 6:
        return "Вы должны ходить в детский сад"
    elif age <= 16:
        return "Вы должны учиться в школе"
    elif 17 <= age <= 21:
        return "ВЫ должны учиться в ВУЗе"
    else:
        return "Вам пора работать"

def main():
    age = abs(int(input("Введите Ваш возраст: ")))
    # Вызвать функцию, передав ей возраст пользователя, и положить результат работы функции в переменную
    total = what_to_do(age)
    # Вывести содержимое переменной на экран
    print(total)

if __name__ == "__main__":
    main()
