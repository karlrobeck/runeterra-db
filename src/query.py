from typing import Generic,TypeVar
from .model import BaseModel
T = TypeVar('T')

class Query(Generic[T]):

    def __init__(self,table:T) -> None:
        self.table:BaseModel[T] = table
        self.__query__ = []
        self.__values__ = ''
        self.__table_object__ = globals()[table.__name__]
        self.__sql__ = f'BEGIN; {self.__query__} COMMIT;'

    def select(self,*columns:tuple[T]):
        
        sql_select_syntax = "SELECT {columns} FROM {table}"

        if len(columns) == 0:

            self.__query__.append(
                sql_select_syntax.format(
                    columns=', '.join([
                        x.__query__ for x in self.table.__table_info__.values()
                    ]),
                    table=self.table.__sql_table_name__
                )
            )

            return self

        self.__query__.append(
            sql_select_syntax.format(
                columns=', '.join([
                    x.__query__ for x in columns
                ]),
                table=self.table.__sql_table_name__
            )
        )
        return self
    
    def insert(self,*values:tuple[T]|T):

        sql_insert_syntax = "INSERT INTO {table} ( {columns} ) VALUES ( {values} )"

        if len(values) == 1 and isinstance(values[0],BaseModel):
            self.__values__ = [val.__value__ for val in values[0].__table_info__.values()]

            self.__query__.append(
                sql_insert_syntax.format(
                    table=self.table.__sql_table_name__,
                    columns=', '.join([x.__query__ for x in values[0].__table_info__.values()]),
                    values=', '.join(self.__fillValue(len(self.__values__)))
                )
            )
            return self

        self.__values__ = tuple([x.__value__ for x in values])

        self.__query__.append(
            sql_insert_syntax.format(
                table=self.table.__sql_table_name__,
                columns=', '.join([x.__query__ for x in values]),
                values=', '.join(self.__fillValue(len(self.__values__)))
            )
        )
        return self

    def where(self,conditions:T):

        sql_where_syntax = "WHERE {conditions}"

        self.__query__.append(
            sql_where_syntax.format(
                conditions=conditions.__query__
            )
        )

        return self

    def __fillValue(self,length:int) -> list[str]:

        return ['?' for _ in range(length)]
    
    def __repr__(self) -> str:
        return ' '.join(self.__query__)
    
    def __str__(self) -> str:
        return ' '.join(self.__query__)