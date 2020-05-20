"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():

    def funct(line1, line2):
        # Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
        if type(line1) == str and type(line2) == str:
            # Если строки одинаковые, вернуть 1
            if line1.lower() == line2.lower():
                return "1"
            # Если строки разные и первая длиннее, вернуть 2
            elif line1 != line2 and len(line2) > len(line1):
                return "2"
            # Если строки разные и вторая строка 'learn', возвращает 3
            elif line1 != line2 and line2 == "learn":
                return "3"
            return "Переданные данные - строки, но не удовлетворяют другим условиям задачи"
        else:
            return "0"

    # Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты
    print(funct(11, "мир"))
    print(funct("Привет", 22))
    print(funct("Привет", "привет"))
    print(funct("Привет", "длинное слово"))
    print(funct("Привет", "learn"))
    print(funct("Привет", "мир"))
    
if __name__ == "__main__":
    main()
