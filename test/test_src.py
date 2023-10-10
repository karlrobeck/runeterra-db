from src.orm import *


class Test_System:
    
    class User(BaseModel):
        id:Field[int] = Field(0,primary_key=True)
        name:Field[str] = Field("",required=True)
        first_name:Field[str] = Field("",required=True)
        last_name:Field[str] = Field("",required=True,unique=True)
    
    def test_01(self) -> None:
        """
            Operator test
        """
        test_variable = Field(50)
        
        # Query operator test
        assert (test_variable == 50).__query__ == ' = 50'
        assert (test_variable > 50).__query__ == ' > 50'
        assert (test_variable < 50).__query__ == ' < 50'
        assert (test_variable >= 50).__query__ == ' >= 50'
        assert (test_variable <= 50).__query__ == ' <= 50'
        assert (test_variable != 50).__query__ == ' <> 50'
        
        #operator test
        assert not (test_variable > 50).__operator_result__
        assert not (test_variable < 50).__operator_result__
        assert (test_variable >= 50).__operator_result__
        assert (test_variable <= 50).__operator_result__
        assert (test_variable == 50).__operator_result__
        assert not (test_variable != 50).__operator_result__
        
        return
    
    def test_02(self) -> None:
        """
            Table test
        """
        table_variable = self.User(id=1,name='karl robeck alferez',first_name='karl',last_name='alferez')
        
        assert table_variable.id == 1
        assert table_variable.name == 'karl robeck alferez'
        assert table_variable.first_name == 'karl'
        assert table_variable.last_name == 'alferez'
        
        return
    
    def test_03(self) -> None:
        """
            Query test
        """
        
        return 
    
    def test_04(self) -> None:
        """
            Session test
        """
        
        return 
    
    def test_05(self) -> None:
        """
            ORM test
        """
        
        return 