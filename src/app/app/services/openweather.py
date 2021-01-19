import httpx
import os
from typing import Optional


async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = os.getenv('API_KEY', 'test_key')
    q = f'{city},{state},{country}' if state else f'{city},{country}'
    url = f'{base_url}?q={q}&appid={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']

    return forecast
