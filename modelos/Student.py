from config import Db
from sqlalchemy import Column, Integer, String


class Student(Db.Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    spec = Column(String)
    age = Column(Integer)

    def __init__(self, id, name, spec, age):
        self.id = id
        self.name = name
        self.spec = spec
        self.age = age

    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.name}, Spec: {self.spec}, Age: {self.age}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'spec': self.spec,
            'age': self.age
        }