from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import datetime
import json
#from main import Person
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
class Student(BaseModel):
       id:int
       name:str
       grade:int
       def toJson(self):
             return {'id':self.id,'name':self.name,'grade':self.grade}
students=[Student(id=1,name='sayed',grade='90'),
          Student(id=2,name='sara',grade=80)
          ]      
@app.get('/students')
def getStudents():
       return students
@app.post('/students')
def addStudent(newStudent:Student):
       students.append(newStudent)
       return newStudent
@app.put('/students/{student_id}')
def updateStudent(student_id:int,new_student:Student):
       for student in students:
              if student.id==student_id:
                     student=new_student
                     return student
       return {'error':'no student found'}       
@app.delete('/students/{student_id}')
def deleteStudent(student_id:int):
       for student in students:
              if(student.id==student_id):
                  students.remove(student) 
                  return{'done':'student deleted'}     
       return {'error':'student not founded'}      
@app.get('/test')
def testList():
       return json.dumps(students[0].toJson())


class Person:
    age:int
    def __init__(self,age) -> None:
        self.age=age
    def toJson(self):
          return f'{self.age}' 
       # nums={'a','f','c','a'}
       # nums.add('h')
       #len()
       # numbers=[1,2,3,4,5]
       # nums=numbers[:2]
       # indexes=[-1,-2,-3,-4,-5]
       # i=-1
       # coord=(4,5)
       # coord=(6,7)
       # # for i in indexes:
       # #   nums.append(numbers[i])
       #return nums[0]
def getRandom(*,ran,v):
       return ran+v
def sumnums(nums):
       result=0
       for i in nums:
              result+=i

       return result
       # nums=set()
       # for i in range(ran):
       #        nums.add(str(i))
       # removedItem=nums.pop()
       # return removedItem
       # for x in nums:
       #   return x       

#list [],tubles (),set {},dict {}

       

