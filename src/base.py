class BaseSQL:
    """
    Base class for SQL operations.
    """

    __value__ = None  # Placeholder for the value
    __query__: str = ''  # SQL query string
    __name__: str = ''  # Name of the object

    def __sql__(self) -> str:
        """
        Get the SQL query string.

        Returns:
            str: The SQL query string.
        """
        return self.__query__
    
    def __info__(self) -> dict:
        """
        Get a dictionary containing the instance variables of an object.

        Returns:
            dict: A dictionary containing the instance variables (attributes) of the object.
        """
        return vars(self.__class__())

    def __repr__(self) -> str:
        """
        Get a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return str(self.__value__)

    def __str__(self) -> str:
        """
        Get a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return str(self.__value__)
    
def sql(data:BaseSQL):
    """
    Get the SQL query string from an object.

    Args:
        data (BaseSQL): An object with a __sql__ method to retrieve the SQL query string.

    Returns:
        str: The SQL query string.
    """
    assert isinstance(data,BaseSQL), 'Object not supported'
        
    return data.__sql__()