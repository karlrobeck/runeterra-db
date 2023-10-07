from .base import BaseSQL

class BaseModel(BaseSQL):

    def __init__(self) -> None:
        super().__init__()