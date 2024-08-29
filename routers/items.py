from fastapi import APIRouter
router=APIRouter()
@router.get('/items')
def getUesrs():
    return {
        'items':'all items will be showed here'
    }
@router.post('/items')
def addUser():
    return {
        'items':'item info from new item'
    }