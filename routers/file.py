from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@router.post("/uploadfile/")
def create_upload_file(myfile: UploadFile):
    contents=myfile.file.read()
    #myImage=open('image.jpg','w')
    return {"filename":contents[0]}