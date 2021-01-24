from typing import Optional, List

import fastapi
from fastapi import Depends

from ..models.location import Location
from ..models.report import Report, ReportSubmittal
from ..models.validation_error import ValidationError
from ..services import openweather, report
router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def get_weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather.get_report(loc.city, loc.state, loc.country, units)

    except ValidationError as err:
        return fastapi.Response(content=err.error_msg, status_code=err.status_code)

    except Exception as err:
        return fastapi.Response(content='Error processing your request.', status_code=500)


@router.get('/api/reports', name='all_reports')
async def reports_get() -> List[Report]:
    return await report.get_reports()


@router.post('/api/reports', name='add_report', status_code=201)
async def reports_add(report_submittal: ReportSubmittal) -> Report:
    desc = report_submittal.description
    loc = report_submittal.location
    return await report.add_report(desc, loc)
