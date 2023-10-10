from .base import BaseSQL
from .field import DATATYPES, Field
from typing import Any,Self
import copy

class SampleTable:
    name:str = ''

class BaseModel(BaseSQL):
    __table_info__:dict[str,Field[Any]] = {}
    
    def __init__(self,**kwargs:Any) -> None:
        
        if self.__class__ == BaseModel:
            raise Exception("BaseModel should not be initialize without a subclass")        
        
        for key in self.__class__.__annotations__.keys():
            default_field:Field[Any] = getattr(self,key)
            _field:Field[Any] = copy.deepcopy(default_field)
            if key in kwargs.keys():
                _field.__values__ = kwargs[key]
            _field.__name__ = key
            _field.__sql__ = f"{_field.__name__} {DATATYPES[_field.__type__.__name__]} {' '.join(_field.__sql_constraints__)}".strip()
            self.__table_info__.update({key:_field})
            setattr(self,key,_field) 
        
             

