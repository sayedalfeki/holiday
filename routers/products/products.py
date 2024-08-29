from fastapi import APIRouter
router=APIRouter()
@router.get('/products')
def getUesrs():
    return {
        'products':'all items will be showed here'
    }
@router.post('/products')
def addUser():
    return {
        'product':'item info from new item'
    }