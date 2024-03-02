#Натуральные числа , состоящие из чётных и нечётных чередующихся цифр . Для каждого числа минимальную и максимальную цифру вывести прописью.ВАРИАНТ-20(С помощью регулярного выражения)
import re


words = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}


with open("lorem.txt", 'r') as file:
    line = file.read()
    numbers = re.findall(r'\b(?:\d*[13579]\d*[02468]\d*|\d*[02468]\d*[13579]\d*)\b', line)
    print(numbers)
    if len(numbers)==0:
        print('<<END>>')
    for number in numbers:
        min_digit = min(number)
        max_digit = max(number)
        number_words = ' '.join([words[digit] for digit in number])
        min_digit_word = words[min_digit]
        max_digit_word = words[max_digit]
        print(f"Число: {number_words} ==> Минимальная цифра: {min_digit_word} ==> Максимальная цифра: {max_digit_word}")
