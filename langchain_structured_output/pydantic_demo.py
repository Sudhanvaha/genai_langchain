from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name : str='Sudhanva'
    age : Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,description="A decimal value representing the cgpa of the student")


new_student={'email':'abc@hotmail.com','cgpa':9}

student=Student(**new_student)
print(student.age)

student_dict=dict(student)
print(student_dict['name'])

student_json=student.model_dump_json()
print(student_json)