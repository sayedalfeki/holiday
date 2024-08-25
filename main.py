from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
# from routers import hrholiday, users,items,file
# from routers.products import products
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
@app.get('/api')
def welcomeApp():
    return {
        'greeting':'welcome to our app'
    }
@app.get('/isholiday')
def isHoliday(year:int,month:int,day:int):
    selectedDate=datetime.datetime(year=year,month=month,day=day)
    dates=[datetime.datetime(year=2024,month=7,day=11),datetime.datetime(year=2024,month=9,day=19)]
    return {'isHoliday':dates.__contains__(selectedDate)}    
# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(products.router)
# app.include_router(file.router)
# app.include_router(hrholiday.router)

# import pandas as pd
# app=FastAPI()
# @app.get('/pandas')
# def makeData():
#     data={'calories':[420,380,390],
#           'duration':[50,40,45]}
#     df=pd.DataFrame(data)
#     return df
# class Person:
#     age:int
#     def __init__(self,age) -> None:
#         self.age=age
