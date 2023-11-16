FROM python:3.11

WORKDIR /site
ENV PYTHONUNBUFFERED=1 JANGO_SETTINGS_MODULE=skillguide.settings

COPY ./skillguide /site/skillguide
COPY ./requirements.txt /site
COPY ./README.md /site

RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /site/skillguide

EXPOSE 8000

CMD sh -c 'python manage.py migrate && python manage.py runserver 0.0.0.0:8000'
