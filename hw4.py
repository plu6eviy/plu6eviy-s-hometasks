name = str(input('Введите ваше имя:'))
age = int(input('Введите ваш возраст:'))
input_txt = ''
input_txt += f'Привет, {name.title()}. Teбе {age} лет '
print(input_txt)


def check_input(name):
    if len(name) == 0:
        return "Имя не введено"
    else:
        return 'Имя введено'


def determine_age_expression(age):
    if age == 1 or (age % 10 == 1 and age != 11):
        return 'год'
    elif 1 < age < 5:
        return 'года'
    else:
        return 'лет'


def check_name(name):
    if not name:
        while True:
            name = input("Вы не ввели ваше имя. Введите имя пожалуйста:")
            result = check_input(name)
            if result == "Имя введено":
                break


def chek_input_age(age, input_txt=None):
    if age <= 0:
        input_txt += 'Возраст не может быть меньше либо равно 0.'
    elif age < 14:
        input_txt += 'Вам запрещено пользоваться программой так как вам меньше 14 лет.'
    if not input_txt:
        if 16 <= age <= 17:
            input_txt += ' Не забудь получить первый паспорт.'
        elif 25 <= age <= 26:
            input_txt += ' Пора бы поменять паспорт.'
        elif 45 <= age <= 46:
            input_txt += ' Пора бы второй раз поменять паспорт.'

'''def clean_spaces(input_string):
    return input_string.strip()

def check_name(name):
    name = clean_spaces(name)
    if not name:
        return "Вы не ввели имя."
    elif len(name) < 3:
        return "Минимальная длинна имени - 3 символа."
    elif len(name.split(' ')) != len(name):
        return "В имени между буквами допускается только 1 пробел."
    else:
        return ''

def check_age(age):
    age = clean_spaces(age)
    if not age:
        return "Вы не ввели возраст."
    elif not age.isdigit():
        return "Возраст должен быть числом."
    elif int(age) <= 0:
        return "Возраст не может быть меньше либо равно 0."
    elif 16 <= int(age) <= 17:
        return 'Вам запрещено пользоваться программой так как вам меньше 14 лет.'
    else:
        return ''

def passport_advice():
    return "Если вы не успели получить или заменить паспорт, то обратитесь в выдающую структуру для получения подробной информации"

def main():
    name = ''
    age = ''

    while True:
        name = clean_spaces(input("Введите ваше имя: "))
        age = clean_spaces(input("Введите ваш возраст: "))
        error_name = check_name(name)
        error_age = check_age(age)
        if error_name and error_age:
            print(f"{error_name} {error_age}")
        elif error_name:
            print(error_name)
        elif error_age:
            print(error_age)
        else:
            print(f"Привет {name.title()}. Тебе {age} лет.")
            break

main()'''