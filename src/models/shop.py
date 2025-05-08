from sqlmodel import SQLModel, Field, Relationship


class ProductCategory(SQLModel, table=True):
    __tablename__ = "product_category"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field(default=None)
    products: list["Product"] = Relationship(back_populates="category")


class Product(SQLModel, table=True):
    __tablename__ = "product"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field(default=None)
    price: float = Field(default=0.0)
    category_id: int = Field(foreign_key="product_category.id")
    category: ProductCategory = Relationship(back_populates="products")

class Order(SQLModel, table=True):
    __tablename__ = "order"
    id: int = Field(default=None, primary_key=True)
    created_at: str = Field(default=None)
    updated_at: str = Field(default=None)
    items: list["OrderItem"] = Relationship(back_populates="order")
    payment_status: str = Field(default="pending")
    
    def total_price(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)

class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    order: Order = Relationship(back_populates="items") 
    product_id: int = Field(foreign_key="product.id")
    quantity: int = Field(default=1)
    product: Product = Relationship(back_populates="orders")