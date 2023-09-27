from datetime import datetime

date_string = "Wed, 13 Sep 2023 11:43:52 GMT"
date_format = '%a, %d %b %Y %H:%M:%S %Z'

date = datetime.strptime(date_string, date_format)

months = (
'Января', 'Февраля', 'Марта', 'Aпреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря')

f'{date.day} {months[date.month - 1]} {date.year}'
pass
print(date)
