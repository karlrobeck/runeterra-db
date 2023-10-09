from typing import Generic,TypeVar
from .query import Query
import sqlite3
import pandas as pd

T = TypeVar('T')

class Session(Generic[T]):

    def __init__(self,engine:sqlite3.Connection) -> None:
        self.cursor = engine.cursor()
        self.connection = engine
        self.__query_obj__ = None
        pass

    def __enter__(self):
        return self
    
    def __exit__(self,exc_type, exc_value, exc_traceback):
        if exc_type:
            print(exc_type)
        if exc_value:
            print(exc_value)
        if exc_traceback:
            print(exc_traceback)
        self.cursor.close()
        return self
    
    def execute(self,sql:Query[T]):
        sql.__values__ = [f"'{item}'" if isinstance(item, str) else item for item in sql.__values__]
        self.cursor = self.cursor.execute(str(sql),sql.__values__)
        self.__query_obj__ = sql.__table_object__
        return self
    
    def fetchall(self,to:str='base_model'):
        columns = tuple([x[0] for x in self.cursor.description])
        data = self.cursor.fetchall()
        if to == 'base_model':
            return self.__query_obj__(**dict(zip(columns,data[0])))
        
        if to == 'pandas':
            if len(data) == 1:
                return pd.DataFrame(data=[data[0]],columns=columns)
            return pd.DataFrame(data=data,columns=columns)
    
    def commit(self):
        return self.connection.commit()