import src.orm as db

class SampleTable(db.BaseModel):
    name:db.Field[int] = db.Field(1)
    

if __name__ == "__main__":
    test = SampleTable(name=123123213)