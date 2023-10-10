from typing import (
    Any,
)
class BaseSQL:
    __values__ = Any
    __sql__:str = ""
    __query__:str | list[str] = ""
    __name__:str = ""

    def __str__(self) -> str:
        return str(self.__values__)