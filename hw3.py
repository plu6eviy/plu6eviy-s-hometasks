"""Программа, которая
- Запрашивает у пользователя имя и возраст;
- Проверяет минимальный возраст 14;
- Проверяет имя на пустоту;
- Проверяет возраст на отрицательное число или 0;
- Проверяет, что имя введено и минимальное количество символов в имени — 3;
* Проверяет, что возраст 16-17 лет и нужно не забыть получить первый паспорт;
    возраст 25-26 лет и нужно заменить паспорт;
    возраст 45-46 лет и нужно второй раз заменить паспорт;
- Выводит либо текст с ошибкой, либо приветствие пользователя с его именем (с заглавной буквы),
    указанием возраста и *советом получить/заменить паспорт (если совет актуален).
* Совет с паспортом выводить только в том случае, если отображается приветствие.

Ограничения:
- только один раз можно использовать print


Дополнительная информация, которая может вам пригодиться:
- Можно писать на русском языке текст внутри строк.
- Внутри блока кода в ветвлениях if-elif-else возможно писать еще if-elif-else.
"""
name = str(input('Введите ваше имя:'))
age = int(input('Введите ваш возраст:'))
txt = ''
if not name:
    txt += 'Вы не ввели имя.'
elif len(name) < 3:
    txt += 'Минимальная длинна имени - 3 символа.'
if age <= 0:
    txt += 'Возраст не может быть меньше либо равно 0.'
elif age < 14:
    txt += 'Вам запрещено пользоваться программой так как вам меньше 14 лет.'


if not txt:
    txt = f"Привет {name.title()}. Тебе {age} лет."

    if 16 <= age <=17:
        txt += ' Не забудь получить первый паспорт.'
    elif 25 <= age <= 26:
        txt += ' Пора бы поменять паспорт.'
    elif 45 <= age <= 46:
        txt += ' Пора бы второй раз поменять паспорт.'

print(txt)

