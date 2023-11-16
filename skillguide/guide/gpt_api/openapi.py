import json
import os

import aiohttp

SERVER_GPT = os.environ.get('SERVER_GPT')


async def answer(content: str):

    data = {
        'content': content,
        'model': None,
        'provider': 'Default'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=f'{SERVER_GPT}/chatgpt/answer',
                                data=json.dumps(data),
                                headers={"Content-Type": "application/json"}
                                ) as response:
            if response.status == 200:
                return await response.json()

            return {'result': 'Не удалось получить ответ от GPT модели'}