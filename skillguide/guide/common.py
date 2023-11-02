from datetime import datetime

Title = 'Python Skills Tracker'

SERVER_ARD = 'http://127.0.0.1:5000'


def index_dict():
    return {
        'title': Title,
    }


def formatted_salary(salary: float, prefix: str):
    return f'{prefix} {int(salary):_} ₽'.replace('_', ' ') if salary > 0 else ''


def string_hh_to_datetime(date_string):
    months = (
        'Января', 'Февраля', 'Марта', 'Aпреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
        'Декабря')

    date = datetime.fromisoformat(date_string,)

    return f'{date.day} {months[date.month - 1]} {date.year}'
