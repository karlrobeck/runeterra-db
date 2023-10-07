import src.orm as test


def test_Field_Contraints():
    
    sample_field = test.Field(primary_key=True)
    assert sample_field.__constraint__() == "PRIMARY KEY"

    sample_field = test.Field(required=True)
    assert sample_field.__constraint__() == "NOT NULL"

    sample_field = test.Field(unique=True)
    assert sample_field.__constraint__() == "UNIQUE"

    sample_field = test.Field(required=True,unique=True)
    assert sample_field.__constraint__() == "NOT NULL UNIQUE"

    sample_field = test.Field(default='test')
    assert repr(sample_field) == 'test'

    sample_field = test.Field(default='test')
    assert sample_field.__info__() == {'primary_key': False, 'required': False, 'unique': False, '__value__': None, '__name__': '', 'type': None, '__query__': ''}

class User(test.BaseModel):
    id:test.Field[int] = test.Field(primary_key=True)
    username:test.Field[str] = test.Field(required=True,unique=True)
    password:test.Field[str] = test.Field(required=True)
    first_name:test.Field[str] = test.Field(required=True)
    last_name:test.Field[str] = test.Field(required=True)
    email:test.Field[str] = test.Field(required=True)

def test_baseModel():

    sampleTable = User()
    assert User().__sql__() == "CREATE TABLE user ( id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL );"

    assert sampleTable.columns() == ['id', 'username', 'password', 'first_name', 'last_name', 'email']

    assert sampleTable.col_info() == User().col_info()

    assert sampleTable.__name__() == 'user'