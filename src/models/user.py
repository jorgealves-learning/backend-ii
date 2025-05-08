from sqlmodel import Field, Relationship, SQLModel
from models.shop import Order

class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    password_hash: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    orders: list["Order"] = Relationship(back_populates="user")
    
    def verify_password(self, password: str) -> bool:
        # Implement password verification logic here
        pass

    def set_password(self, password: str) -> None:
        # Implement password hashing and setting logic here
        pass
