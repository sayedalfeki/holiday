from fastapi import APIRouter
import datetime
router=APIRouter()

@router.get('/isholiday')
def isHoliday(year:int,month:int,day:int):
    selectedDate=datetime.datetime(year=year,month=month,day=day)
    dates=[datetime.datetime(year=2024,month=7,day=11),datetime.datetime(year=2024,month=7,day=23)]
    return {'isHoliday':dates.__contains__(selectedDate)}
