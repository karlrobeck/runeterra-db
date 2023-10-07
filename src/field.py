from .operators import Operators
from typing import TypeVar,Generic

T = TypeVar('T')

class Field(Generic[T],Operators):
    
    def __init__(
        self,
        default=None,
        default_factory=None,
        optional=False,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=dict(),
        kw_only=False,
        primary_key:bool = False,
        required:bool = False,
        unique:bool = False,
        name:str=''
    ) -> None:
        if default:
            self.__value__ = default

        self.__repr = repr
        self.__name__ = name
        self.__primary_key__ = primary_key
        self.__required__ = required
        self.__unique__ = unique
        self.__type__ = type(default)
        self.__query__ = self.__constraint__()

    def __repr__(self) -> str:
        if self.__repr:
            return super().__repr__()
        else:
            return ''
        
    def __constraint__(self) -> str:
        """
        Return constraints field as a string.

        Returns:
            str: The constraints field as a string.
        """
        constraints = []

        if self.__primary_key__:
            constraints.append("PRIMARY KEY")
        if self.__required__:
            constraints.append("NOT NULL")
        if self.__unique__:
            constraints.append("UNIQUE")

        return " ".join(constraints)
