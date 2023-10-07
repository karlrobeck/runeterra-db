import src.operators as operation
from src.base import sql

def test_Arithmetic():
    arithmetic = operation.Arithmetic()
    arithmetic.__value__ = 5

    # Addition test
    addition_result = arithmetic + 5
    print(addition_result)
    assert sql(addition_result) == '5 + 5', f"Addition test failed. Got: {addition_result}"

    # Subtraction test
    subtraction_result = arithmetic - 3
    assert sql(subtraction_result) == '10 - 3', f"Subtraction test failed. Got: {subtraction_result}"

    # Multiplication test
    multiplication_result = arithmetic * 4
    assert sql(multiplication_result) == '7 * 4', f"Multiplication test failed. Got: {multiplication_result}"

    # Division test
    division_result = arithmetic / 2
    assert sql(division_result) == '28 / 2', f"Division test failed. Got: {division_result}"

    # Modulus test
    modulus_result = arithmetic % 7
    assert sql(modulus_result) == '14.0 % 7', f"Modulus test failed. Got: {modulus_result}"

    print("All arithmetic operation tests passed!")

def test_Bitwise():

    obj = operation.Bitwise()
    obj.__value__ = 5

    # Bitwise AND test
    and_result = obj & 3
    assert sql(and_result) == '5 & 3', f"Bitwise AND test failed. Got: {and_result}"

    # Bitwise OR test
    or_result = obj | 6
    assert sql(or_result) == '1 | 6', f"Bitwise OR test failed. Got: {or_result}"

    # Bitwise XOR test
    xor_result = obj ^ 2
    assert sql(xor_result) == '7 ^ 2', f"Bitwise XOR test failed. Got: {xor_result}"

    print("All bitwise operation tests passed!")

def test_Comparison():
    compare = operation.Comparison()
    compare.__name__ = 'apple'

    # Equal test
    equal_result = compare == "apple"
    assert sql(equal_result) == 'apple = apple', f"Equal test failed. Got: {equal_result}"

    # Greater than test
    greater_than_result = compare > "banana"
    assert sql(greater_than_result) == 'apple > banana', f"Greater than test failed. Got: {greater_than_result}"

    # Less than test
    less_than_result = compare < "cherry"
    assert sql(less_than_result) == 'apple < cherry', f"Less than test failed. Got: {less_than_result}"

    # Greater than or equal to test
    greater_than_equal_result = compare >= "apple"
    assert sql(greater_than_equal_result) == 'apple >= apple', f"Greater than or equal to test failed. Got: {greater_than_equal_result}"

    # Less than or equal to test
    less_than_equal_result = compare <= "apple"
    assert sql(less_than_equal_result) == 'apple <= apple', f"Less than or equal to test failed. Got: {less_than_equal_result}"

    # Not equal test
    not_equal_result = compare != "kiwi"
    assert sql(not_equal_result) == 'apple <> kiwi', f"Not equal test failed. Got: {not_equal_result}"

    print("All comparison operation tests passed!")

def test_logical_operations():
    logical = operation.Logical()

    # Test _all
    all_result = logical._all("SELECT * FROM table")
    assert all_result == "ALL ( SELECT * FROM table )", f"_all test failed. Got: {all_result}"

    # Test _and
    and_result = logical._and("condition1", "condition2")
    assert and_result == "condition1 and condition2", f"_and test failed. Got: {and_result}"

    # Test _any
    any_result = logical._any("SELECT column FROM table")
    assert any_result == "ANY ( SELECT column FROM table )", f"_any test failed. Got: {any_result}"

    # Test _between
    between_result = logical._between("value1", "value2")
    assert between_result == "BETWEEN value1 and value2", f"_between test failed. Got: {between_result}"

    # Test _exist
    exist_result = logical._exist("SELECT * FROM another_table")
    assert exist_result == "EXISTS ( SELECT * FROM another_table )", f"_exist test failed. Got: {exist_result}"

    # Test _in
    in_result = logical._in("SELECT column FROM another_table")
    assert in_result == "IN SELECT column FROM another_table", f"_in test failed. Got: {in_result}"

    # Test _like
    like_result = logical._like("'pattern%'")
    assert like_result == "LIKE 'pattern%'", f"_like test failed. Got: {like_result}"

    # Test _or
    or_result = logical._or("condition1", "condition2")
    assert or_result == "condition1 or condition2", f"_or test failed. Got: {or_result}"

    # Test _not
    not_result = logical._not("condition")
    assert not_result == "NOT condition", f"_not test failed. Got: {not_result}"

    # Test _some
    some_result = logical._some("SELECT value FROM some_table")
    assert some_result == "SOME ( SELECT value FROM some_table )", f"_some test failed. Got: {some_result}"

    print("All logical operation tests passed!")

def test_compound():

    compound = operation.Compound()
    compound.__value__ = 5

    # Test in-place addition
    compound += 5
    assert sql(compound) == '5 += 5', f"In-place addition test failed. Got: {compound.value}"

    # Test in-place subtraction
    compound -= 5
    assert sql(compound) == '10 -= 5', f"In-place subtraction test failed. Got: {compound.__value__}"

    # Test in-place multiplication
    compound *= 5
    assert sql(compound) == '5 *= 5', f"In-place multiplication test failed. Got: {compound.__value__}"

    # Test in-place division
    compound /= 5
    assert sql(compound) == '25 /= 5', f"In-place division test failed. Got: {compound.__value__}"

    # Test in-place modulus
    compound %= 5
    assert sql(compound) == '5.0 %= 5', f"In-place modulus test failed. Got: {compound.__value__}"

    # Test in-place bitwise AND
    compound &= 5
    assert sql(compound) == '0.0 &= 5', f"In-place bitwise AND test failed. Got: {compound.__value__}"

    # Test in-place bitwise OR
    compound |= 5
    assert sql(compound) == '0.0 |*= 5', f"In-place bitwise OR test failed. Got: {compound.__value__}"

    # Test in-place bitwise XOR
    compound ^= 5
    assert sql(compound) == '0.0 ^-= 5', f"In-place bitwise XOR test failed. Got: {compound.__value__}"

    print("All in-place operation tests passed!")

