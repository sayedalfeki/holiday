from fastapi import APIRouter,Query,Path,Cookie,Form,Header
from typing import Annotated
from pydantic import BaseModel
import json
router=APIRouter()
class Users(BaseModel):
    userId:int
    name:str
    address:str|None=None
@router.get('/user/auth')
def getCookies(ads_id:Annotated[str,Header()]):
    return {'ads_id':ads_id}
@router.get('/users/{me}')
def getUesrs(me:Annotated[int,Path(title='id to get user')],name:Annotated[str|None,Query(title='query string',min_length=3,max_length=6)]=...):
    return {
        'users':name
    }
@router.post('/users')
def addUser(users:Users)->Users:
    
    return users
    
@router.put('/users')
def loginUser(name:Annotated[str,Form()],password:Annotated[str,Form()]):
    return {
        'name':name,
        'password':password
    }
@router.get('/users/test')
def testUser():
    return {
        'test':True
    }
