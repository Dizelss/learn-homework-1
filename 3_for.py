"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

    school_progress = [
        {"school_class": "1a", "scores": [3, 5, 4, 2, 7, 10, 12, 12, 11, 10, 5, 7]},
        {"school_class": "1b", "scores": [10, 8, 6, 7, 7, 3, 5, 8, 9, 4, 9, 8]},
        {"school_class": "2a", "scores": [7, 6, 4, 6, 5, 10, 11, 7, 10, 12, 3, 11]},
        {"school_class": "3c", "scores": [9, 8, 6, 5, 7, 10, 12, 8, 9, 10, 4, 6]},
    ]
    sum_middle_score_school = 0
    for one_class in school_progress:
        # Посчитать и вывести средний балл по каждому классу
        middle_score_class = round(sum(one_class["scores"]) / len(one_class["scores"]), 1)
        print(f"Средняя оценка класса {one_class['school_class']}: {middle_score_class}")

        # Посчитать и вывести средний балл по всей школе
        sum_middle_score_school += middle_score_class
    print(f"Средняя оценка по всей школе: {round(sum_middle_score_school / len(school_progress), 1)}")

    ################################
    # Альтернативный вариант решения
    ################################
    # count = 0
    # sum_middle_score_school = 0
    # for one_class in school_progress:
    #     # Посчитать и вывести средний балл по каждому классу
    #     sum_scoress_one_class = 0
    #     count += 1
    #     for score_class in one_class["scores"]:
    #         sum_scoress_one_class += score_class
    #     middle_score_class = sum_scoress_one_class / len(one_class["scores"])
    #     sum_middle_score_school += middle_score_class
    #     print(f"Средняя оценка класса {one_class['school_class']}: {round(middle_score_class, 1)}")
    #
    # # Посчитать и вывести средний балл по всей школе
    # print(f"Средняя оценка по всей школе: {round(sum_middle_score_school / count,1)}")
    
if __name__ == "__main__":
    main()
