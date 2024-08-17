from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)
@app.get('/')
def isHoliday(year,month,day):
        dates=[datetime.date(2024,7,11),datetime.date(2024,9,17),
               datetime.date(2024,10,6),datetime.date(2024,11,11),
           datetime.date(2024,12,12)]
        selectedDate=datetime.date(year=int(year),month=int(month),day=int(day))
        return {'result':dates.__contains__(selectedDate)}

