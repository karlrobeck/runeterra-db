from .operators import (
    SQLOperators
)
from typing import Any,TypeVar,Generic,Self

T = TypeVar('T')

DATATYPES:dict[str,str] = {
    'int':'INTEGER',
    'float':'REAL',
    'str':'TEXT',
    'bytes':'BLOB',
}

class Field(SQLOperators,Generic[T]):

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

        self.__sql_primary_key__:str = "PRIMARY KEY" if primary_key else ""
        self.__sql_required__:str = "NOT NULL" if required else ""
        self.__sql_unique__:str = "UNIQUE" if unique else ""
        self.__sql_constraints__:list[str] = []
        
        for constraint in [self.__sql_primary_key__,self.__sql_required__,self.__sql_unique__]:
            if constraint:
                self.__sql_constraints__.append(constraint)

        self.__sql__:str = f"{self.__name__} {DATATYPES[self.__type__.__name__]} {' '.join(self.__sql_constraints__)}".strip()

    def set(self,values:T) -> Self:
        self.__values__:T = values
        return self
    
    def get(self) -> T:
        return self.__values__
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__name__}={self.__values__})"