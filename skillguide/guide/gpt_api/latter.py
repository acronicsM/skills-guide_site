import re

from .openapi import answer as openapi_answer
from .yandexgpt import answer as yandexgpt_answer


async def get_letter(description, gpt):
    if gpt == 'openai':
        answer = await get_openapi_answer(description)
        return answer['result']

    if gpt == 'yandex':
        answer = await get_yandex_answer(description)
        return answer['result']


async def get_openapi_answer(description: dict):
    description_text = remove_html_tags(description['description'])

    content = f'''
    Мне нужно приложить сопроводительное письмо к моему резюме для отклика на вакансию:
    {description_text}
    '''

    return await openapi_answer(content=content)


async def get_yandex_answer(description: dict):
    description_text = remove_html_tags(description['description'])

    content = f'Напиши такое письмо на вакансию:\n{description_text}'
    instruction = 'Мне нужно приложить сопроводительное письмо к моему резюме для отклика на вакансию'

    return await yandexgpt_answer(content=content, instruction=instruction)


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
