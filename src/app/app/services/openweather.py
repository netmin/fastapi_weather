import httpx
import os
from typing import Optional

from ..infrastructure.weather_cache import get_weather, set_weather


from logging import getLogger

_logger = getLogger(__name__)


async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    _logger.info('INFO')
    _logger.warning('WARN')
    _logger.error('ERR')
    _logger.debug('Debug')
    if forecast := get_weather(city, state, country, units):
        _logger.error(f'FORECAST {forecast}')
        return forecast

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = os.getenv('API_KEY', 'test_key')
    q = f'{city},{state},{country}' if state else f'{city},{country}'
    url = f'{base_url}?q={q}&appid={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']

    set_weather(city, state, country, units, forecast)

    return forecast
