from .base import BaseSQL

class Arithmetic(BaseSQL):
    """
    Represents arithmetic operations as SQL queries.

    This class inherits from BaseSQL and provides methods for performing
    arithmetic operations and generating corresponding SQL query strings.
    """

    def __add__(self, other):
        """
        Perform addition operation and generate an SQL query string.

        Args:
            other: The value to add.

        Returns:
            Arithmetic: A new instance of Arithmetic with the updated query string.
        """
        self.__query__ = f"{self.__value__} + {other}"
        try:
            self.__value__ = self.__value__ + other
        except:
            pass
        return self

    def __sub__(self, other):
        """
        Perform subtraction operation and generate an SQL query string.

        Args:
            other: The value to subtract.

        Returns:
            Arithmetic: A new instance of Arithmetic with the updated query string.
        """
        self.__query__ = f"{self.__value__} - {other}"
        try:
            self.__value__ = self.__value__ - other
        except:
            pass
        return self

    def __mul__(self, other):
        """
        Perform multiplication operation and generate an SQL query string.

        Args:
            other: The value to multiply.

        Returns:
            Arithmetic: A new instance of Arithmetic with the updated query string.
        """
        self.__query__ = f"{self.__value__} * {other}"
        try:
            self.__value__ = self.__value__ * other
        except:
            pass
        return self

    def __truediv__(self, other):
        """
        Perform division operation and generate an SQL query string.

        Args:
            other: The value to divide by.

        Returns:
            Arithmetic: A new instance of Arithmetic with the updated query string.
        """
        self.__query__ = f"{self.__value__} / {other}"
        try:
            self.__value__ = self.__value__ / other
        except:
            pass
        return self

    def __mod__(self, other):
        """
        Perform modulus operation and generate an SQL query string.

        Args:
            other: The value to calculate the modulus with.

        Returns:
            Arithmetic: A new instance of Arithmetic with the updated query string.
        """
        self.__query__ = f"{self.__value__} % {other}"
        try:
            self.__value__ = self.__value__ % other
        except:
            pass
        return self

    
class Bitwise(BaseSQL):
    """
    Represents bitwise operations as SQL queries.

    This class inherits from BaseSQL and provides methods for performing
    bitwise operations and generating corresponding SQL query strings.
    """

    def __and__(self, other):
        """
        Perform bitwise AND operation and generate an SQL query string.

        Args:
            other: The value to perform the AND operation with.

        Returns:
            Bitwise: A new instance of Bitwise with the updated query string.
        """
        self.__query__ = f"{self.__value__} & {other}"
        try:
            self.__value__ = self.__value__ & other
        except:
            pass
        return self

    def __or__(self, other):
        """
        Perform bitwise OR operation and generate an SQL query string.

        Args:
            other: The value to perform the OR operation with.

        Returns:
            Bitwise: A new instance of Bitwise with the updated query string.
        """
        self.__query__ = f"{self.__value__} | {other}"
        try:
            self.__value__ = self.__value__ | other
        except:
            pass
        return self

    def __xor__(self, other):
        """
        Perform bitwise XOR operation and generate an SQL query string.

        Args:
            other: The value to perform the XOR operation with.

        Returns:
            Bitwise: A new instance of Bitwise with the updated query string.
        """
        self.__query__ = f"{self.__value__} ^ {other}"
        try:
            self.__value__ = self.__value__ ^ other
        except:
            pass
        return self
    
class Comparison(BaseSQL):
    """
    Represents comparison operations as SQL queries.

    This class inherits from BaseSQL and provides methods for performing
    comparison operations and generating corresponding SQL query strings.
    """

    def __eq__(self, other) -> bool:
        """
        Perform equal comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for equality.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} = {other}"
        try:
            self.__value__ = self.__value__ == other
        except:
            pass
        return self
    
    def __gt__(self, other) -> bool:
        """
        Perform greater-than comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for greater-than.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} > {other}"
        try:
            self.__value__ = self.__value__ > other
        except:
            pass
        return self

    def __lt__(self, other) -> bool:
        """
        Perform less-than comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for less-than.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} < {other}"
        try:
            self.__value__ = self.__value__ < other
        except:
            pass
        return self

    def __ge__(self, other) -> bool:
        """
        Perform greater-than-or-equal-to comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for greater-than-or-equal-to.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} >= {other}"
        try:
            self.__value__ = self.__value__ >= other
        except:
            pass
        return self

    def __le__(self, other) -> bool:
        """
        Perform less-than-or-equal-to comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for less-than-or-equal-to.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} <= {other}"
        try:
            self.__value__ = self.__value__ <= other
        except:
            pass
        return self

    def __ne__(self, other) -> bool:
        """
        Perform not-equal comparison operation and generate an SQL query string.

        Args:
            other: The value to compare for not-equal.

        Returns:
            Comparison: A new instance of Comparison with the updated query string.
        """
        self.__query__ = f"{self.__name__} <> {other}"
        try:
            self.__value__ = self.__value__ != other
        except:
            pass
        return self
    
class Compound(BaseSQL):
    """
    Represents compound assignment operations as SQL queries.

    This class inherits from BaseSQL and provides methods for performing
    compound assignment operations and generating corresponding SQL query strings.
    """

    def __iadd__(self, other):
        """
        Perform in-place addition operation and generate an SQL query string.

        Args:
            other: The value to add in-place.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} += {other}"
        try:
            self.__value__ += other
        except:
            pass
        return self

    def __isub__(self, other):
        """
        Perform in-place subtraction operation and generate an SQL query string.

        Args:
            other: The value to subtract in-place.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} -= {other}"
        try:
            self.__value__ -= other
        except:
            pass
        return self

    def __imul__(self, other):
        """
        Perform in-place multiplication operation and generate an SQL query string.

        Args:
            other: The value to multiply in-place.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} *= {other}"
        try:
            self.__value__ *= other
        except:
            pass
        return self

    def __itruediv__(self, other):
        """
        Perform in-place division operation and generate an SQL query string.

        Args:
            other: The value to divide in-place by.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} /= {other}"
        try:
            self.__value__ /= other
        except:
            pass
        return self

    def __imod__(self, other):
        """
        Perform in-place modulus operation and generate an SQL query string.

        Args:
            other: The value to calculate the modulus in-place with.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} %= {other}"
        try:
            self.__value__ %= other
        except:
            pass
        return self
    
    def __iand__(self, other):
        """
        Perform in-place bitwise AND operation and generate an SQL query string.

        Args:
            other: The value to perform the bitwise AND operation in-place with.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} &= {other}"
        try:
            self.__value__ &= other
        except:
            pass
        return self

    def __ior__(self, other):
        """
        Perform in-place bitwise OR operation and generate an SQL query string.

        Args:
            other: The value to perform the bitwise OR operation in-place with.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} |*= {other}"
        try:
            self.__value__ |= other
        except:
            pass
        return self

    def __ixor__(self, other):
        """
        Perform in-place bitwise XOR operation and generate an SQL query string.

        Args:
            other: The value to perform the bitwise XOR operation in-place with.

        Returns:
            Compound: A new instance of Compound with the updated query string.
        """
        self.__query__ = f"{self.__value__} ^-= {other}"
        try:
            self.__value__ ^= other
        except:
            pass
        return self
    
class Logical:
    """
    Provides static methods for constructing SQL-like logical expressions.
    """

    @staticmethod
    def _all(statement):
        """
        Create an SQL-like ALL logical expression.

        Args:
            statement (str): The statement to be used in the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"ALL ( {statement} )"

    @staticmethod
    def _and(left, right):
        """
        Create an SQL-like AND logical expression.

        Args:
            left (str): The left side of the expression.
            right (str): The right side of the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"{left} and {right}"

    @staticmethod
    def _any(statement):
        """
        Create an SQL-like ANY logical expression.

        Args:
            statement (str): The statement to be used in the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"ANY ( {statement} )"

    @staticmethod
    def _between(left, right):
        """
        Create an SQL-like BETWEEN logical expression.

        Args:
            left (str): The left value in the range.
            right (str): The right value in the range.

        Returns:
            str: The constructed logical expression.
        """
        return f"BETWEEN {left} and {right}"

    @staticmethod
    def _exist(statement):
        """
        Create an SQL-like EXISTS logical expression.

        Args:
            statement (str): The statement to be used in the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"EXISTS ( {statement} )"

    @staticmethod
    def _in(statement):
        """
        Create an SQL-like IN logical expression.

        Args:
            statement (str): The statement to be used in the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"IN {statement}"

    @staticmethod
    def _like(pattern):
        """
        Create an SQL-like LIKE logical expression.

        Args:
            pattern (str): The pattern to match.

        Returns:
            str: The constructed logical expression.
        """
        return f"LIKE {pattern}"

    @staticmethod
    def _or(left, right):
        """
        Create an SQL-like OR logical expression.

        Args:
            left (str): The left side of the expression.
            right (str): The right side of the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"{left} or {right}"

    @staticmethod
    def _not(condition):
        """
        Create an SQL-like NOT logical expression.

        Args:
            condition (str): The condition to negate.

        Returns:
            str: The constructed logical expression.
        """
        return f"NOT {condition}"

    @staticmethod
    def _some(statement):
        """
        Create an SQL-like SOME logical expression.

        Args:
            statement (str): The statement to be used in the expression.

        Returns:
            str: The constructed logical expression.
        """
        return f"SOME ( {statement} )"
    
class Operators(Arithmetic, Bitwise, Comparison, Compound):
    """
    Represents a combination of different operator classes.

    This class inherits from Arithmetic, Bitwise, Comparison, and Compound,
    providing a combination of various operator types.
    """

    pass
