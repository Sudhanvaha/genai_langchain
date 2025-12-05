from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person:Person={'name':'hai','age':'21'}
#although we have specified age as int,still we passed string still it doesnot show error,here we can just tell that it need to be int,validation is not done by typeddict

print(new_person)