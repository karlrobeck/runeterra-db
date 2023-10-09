from .base import BaseSQL
from .field import Field
from typing import Any
import copy

class SampleTable:
    name:str = ''

class BaseModel(BaseSQL):
    __table_info__:dict[str,Field[Any]] = {}

    def __init__(self,**kwargs:Any) -> None:
        
        if self.__class__ == BaseModel:
            raise Exception("BaseModel should not be initialize without a subclass")        
        
        for key,val in kwargs.items():
            _field:Field[Any] = copy.deepcopy(getattr(self,key))
            _field.set(val)
            _field.__name__ = key
            self.__table_info__.update({key:_field})
            

