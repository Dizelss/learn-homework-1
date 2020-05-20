"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало

* Дополнение от куратора:
Ilya Vorontsov (Куратор, курсы Lean Python), [20.05.20 15:42]
я бы из except убрал print и написал явным образом return None
результат вычисления записал в переменную и в зависимости от того, None это или не None печатал сообщение
    
"""

def get_summ(num_one, num_two):
    try:
        summ = int(num_one) + int(num_two)
        return summ
    except ValueError:
        return None

def print_result (res):
    if res == None:
        print("Переданны переменные, которые не получилось преобразовать в числа")
    else:
        print(f"Результат {res}")
    
if __name__ == "__main__":
    print_result(get_summ(2, 2))
    print_result(get_summ(5, 7))
    print_result(get_summ(3, "3"))
    print_result(get_summ("4", "4"))
    print_result(get_summ("five", 5))
    print_result(get_summ("six", "шесть"))
