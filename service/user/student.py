from service.user.base import BaseUser


class Student(BaseUser):
def __init__(self, id: int):
super().__init__(id)

def get_discount(self):
return 0.5
