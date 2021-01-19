from typing import Optional

import fastapi
from fastapi import Depends

from ..models.location import Location
from ..models.validation_error import ValidationError
from ..services import openweather

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def get_weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather.get_report(loc.city, loc.state, loc.country, units)

    except ValidationError as err:
        return fastapi.Response(content=err.error_msg, status_code=err.status_code)

    except Exception as err:
        return fastapi.Response(content='Error processing your request.', status_code=500)
