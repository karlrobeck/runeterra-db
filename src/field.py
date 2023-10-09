from .base import BaseSQL
from typing import Any,TypeVar,Generic

T = TypeVar('T')

DATATYPES:dict[str,str] = {
    'int':'INTEGER',
    'float':'REAL',
    'str':'TEXT',
    'bytes':'BLOB',
}

class Field(BaseSQL,Generic[T]):

    __field_info__:dict[str,Any]

    def __init__(
        self,
        value:T,
        primary_key:bool=False,
        required:bool=False,
        unique:bool=False
    ) -> None:
        self.__values__:T = value
        self.__type__:type = type(value)

        self.__sql_primary_key:str = "PRIMARY KEY" if primary_key else ""
        self.__sql_required:str = "NOT NULL" if required else ""
        self.__sql_unique:str = "UNIQUE" if unique else ""
        self.__sql_constraints__:list[str] = []
        
        for constraint in [self.__sql_primary_key,self.__sql_required,self.__sql_unique]:
            if constraint:
                self.__sql_constraints__.append(constraint)

        self.__sql__:str = f"{self.__name__} {DATATYPES[self.__type__.__name__]} {' '.join(self.__sql_constraints__)}".strip()

    def set(self,values:T):
        self.__values__:T = values
        return self
    
    def get(self) -> T:
        return self.__values__
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__name__}={self.__values__})"