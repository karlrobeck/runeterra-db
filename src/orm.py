from typing import TypeVar,Generic,_GenericAlias
from .operators import Operators
import sqlite3

T = TypeVar('T')

DATATYPES = {
    'int':'INTEGER',
    'str':'TEXT',
    'float':'REAL',
    'bytes':'BLOB'
}

class Field(Generic[T],Operators): # generics

    def __init__(
        self,
        default=None,
        primary_key:bool = False,
        required:bool = False,
        unique:bool = False,
    ) -> None:
        self.primary_key = primary_key
        self.required = required
        self.unique = unique
        self.__value__ = default
        self.__name__ = ''
        self.type = None
        self.__query__ = ''

    def __constraint__(self) -> str:
        """
        Return constraints field as a string.

        Returns:
            str: The constraints field as a string.
        """
        constraints = []

        if self.primary_key:
            constraints.append("PRIMARY KEY")
        if self.required:
            constraints.append("NOT NULL")
        if self.unique:
            constraints.append("UNIQUE")

        return " ".join(constraints)

class ForeignKey:

    def __init__(self) -> None:
        pass

class BaseModel:

    def __init__(self,**kwargs) -> None:
        pass

    def __sql__(self) -> str:

        columns = []

        for key,val in self.__class__.__annotations__.items():
            getattr(self,key).type = val.__args__[0]
            getattr(self,key).__name__ = key
            if isinstance(val,_GenericAlias):
                columns.append(f'{key} {DATATYPES[val.__args__[0].__name__]} {getattr(self.__class__(),key).__constraint__()}')

        return f"CREATE TABLE {self.__class__.__name__.lower()} ( {', '.join(columns)} );"

    def columns(self):
        return list(self.__class__.__annotations__.keys())

    def __name__(self):
        return self.__class__.__name__.lower()
    
    def col_info(self) -> dict:
        return {key:getattr(self,key).__info__() for key in self.columns()}