class BaseSQL():
    __values__ = None
    __sql__:str
    __query__:str | list[str] = ""
    __name__:str = ""

    def __str__(self) -> str:
        return str(self.__values__)