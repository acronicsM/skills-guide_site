# skills-guide_site

Сайт проекта skills_guide 

![](https://img.shields.io/badge/Django-4.2.7-00CED1)
![](https://img.shields.io/badge/AIOHTTP-3.8.6-DC143C)



## 🛠️ Подготовка в запуску

1. [Download and install Python](https://www.python.org/downloads/) (Version 3.10+ is recommended).

2. Клонируйте репозиторий GitHub:
```bash
git clone https://github.com/acronicsM/skills-guide_site.git
```
3. Перейдите в директорию проекта:
```bash
cd skills-guide_site
```
4. Установите переменные окружения:
```bash
nano .env
```
5. (Рекомендуется) Создайте виртуальную среду Python::
[Python official documentation](https://docs.python.org/3/tutorial/venv.html).


```
python3 -m venv venv
```

6. Активируйте виртуальную среду:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
7. Установите необходимые пакеты Python из `requirements.txt`:

```
pip install -r requirements.txt
```

8. Запустите `manage.py`

## 🙌 Необходимы переменные окружения

1. DB_DRIVER - Драйвер подключения к БД. В текущей конфигурации выбор ограничивается только драйверов postgresql, в случаи указания любого другого драйвера или не указания драйвера вовсе используется бд sqlite:///base1.db
2. POSTGRES_USER - Пользователь для подключения к postgre
3. POSTGRES_PASSWORD - Пароль пользователя для подключения к postgre
4. POSTGRES_HOST - адрес хоста бд postgre
5. POSTGRES_PORT - порт хоста бд postgre
6. POSTGRES_DATABASE_SITE - имя БД postgre
7. ENV - выбор между production (запускает приложение на localhost) и development
8. DEBUG - вкл/выкл режима отладки
9. SECRET_KEY
10. JWT_SECRET_KEY - для доступа к защищеным методам __skills-guide_parser__
11. ALLOWED_HOSTS - список разрешенных хостов
12. SERVER_PARSE - адрес сервиса __skills-guide_parser__
13. SERVER_GPT - адрес сервиса __skills-guide_gpt__