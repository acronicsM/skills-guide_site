from datetime import datetime

Title = 'Путеводитель по навыкам'
Full_Title = 'Путеводитель по навыкам начинающего Python-разработчика: путь в профессию'

# SERVER_ARD = 'http://51.250.48.253:5000'
SERVER_ARD = 'http://127.0.0.1:5000'


def index_dict():
    return {
        'title': Title,
        'full_title': Full_Title,
    }


def formatted_salary(salary: float, prefix: str):
    return f'{prefix} {int(salary):_} ₽'.replace('_', ' ') if salary > 0 else ''


def string_hh_to_datetime(date_string):
    months = (
        'Января', 'Февраля', 'Марта', 'Aпреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
        'Декабря')

    date = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')

    return f'{date.day} {months[date.month - 1]} {date.year}'
