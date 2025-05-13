from enum import Enum

from service.finance import CampusCard


class UserType(Enum):
Student = 'student'
Teacher = 'teacher'


class BaseUser:
def __init__(self, id: int):
self.id = id
self.card = CampusCard()
if self.is_student():
self.type = UserType.Student
elif self.is_teacher():
self.type = UserType.Teacher

def get_discount(self):
raise NotImplementedError

def is_student(self):
return self.id > 10000

def is_teacher(self):
return self.id < 1000
