import fastapi


router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def get_weather():
    return 'weather!'
