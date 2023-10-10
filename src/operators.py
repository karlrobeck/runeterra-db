from .base import BaseSQL
from typing import (
    Any,
    Self
)

class SQLOperators(BaseSQL):
    
    __operator_result__:bool | Any
    
    def __eq__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ == __value
        self.__query__ = f"{self.__name__} = {__value}"
        return self
    
    def __gt__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ > __value
        self.__query__ = f"{self.__name__} > {__value}"
        return self
    
    def __lt__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ < __value
        self.__query__ = f"{self.__name__} < {__value}"
        return self
    
    def __ge__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ >= __value
        self.__query__ = f"{self.__name__} >= {__value}"
        return self
    
    def __le__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ <= __value
        self.__query__ = f"{self.__name__} <= {__value}"
        return self
    
    def __ne__(self, __value: object) -> Self:
        self.__operator_result__ = self.__values__ != __value
        self.__query__ = f"{self.__name__} <> {__value}"
        return self