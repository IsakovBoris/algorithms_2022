"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def counter(number):
    if number <= 9:
        if number % 2:
            return (0, 1)
        else:
            return (1, 0)
    else:
        even, odd = counter(number // 10)
        if (number % 10) % 2:
            odd = odd + 1
        else:
            even = even + 1
    return even, odd


if __name__ == '__main__':
    number = float(input('Введите число:'))
    print('Количество четных и нечетных цифр в числе равно:',counter(number))
