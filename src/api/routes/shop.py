
from fastapi import APIRouter


router = APIRouter(
    prefix="/shop",
    tags=["shop"],
    responses={404: {"description": "Not found"}},
)

@router.get("/products")
async def get_products():
    """
    Get a list of products.
    """
    return {"message": "List of products"}

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    """
    Get a product by ID.
    """
    return {"message": f"Product {product_id}"}

@router.post("/products")
async def create_product(product: dict):
    """
    Create a new product.
    """
    return {"message": "Product created", "product": product}

@router.put("/products/{product_id}")
async def update_product(product_id: int, product: dict):
    """
    Update a product by ID.
    """
    return {"message": f"Product {product_id} updated", "product": product}

@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """
    Delete a product by ID.
    """
    return {"message": f"Product {product_id} deleted"}

@router.get("/orders")
async def get_orders():
    """
    Get a list of orders.
    """
    return {"message": "List of orders"}

@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    """
    Get an order by ID.
    """
    return {"message": f"Order {order_id}"}

@router.post("/orders")
async def create_order(order: dict):
    """
    Create a new order.
    """
    return {"message": "Order created", "order": order}

@router.put("/orders/{order_id}")
async def update_order(order_id: int, order: dict):
    """
    Update an order by ID.
    """
    return {"message": f"Order {order_id} updated", "order": order}

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    """
    Delete an order by ID.
    """
    return {"message": f"Order {order_id} deleted"}

@router.get("/categories")
async def get_categories():
    """
    Get a list of product categories.
    """
    return {"message": "List of product categories"}

@router.get("/categories/{category_id}")
async def get_category(category_id: int):
    """
    Get a product category by ID.
    """
    return {"message": f"Category {category_id}"}


@router.post("/categories")
async def create_category(category: dict):
    """
    Create a new product category.
    """
    return {"message": "Category created", "category": category}

@router.put("/categories/{category_id}")
async def update_category(category_id: int, category: dict):
    """
    Update a product category by ID.
    """
    return {"message": f"Category {category_id} updated", "category": category}

@router.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    """
    Delete a product category by ID.
    """
    return {"message": f"Category {category_id} deleted"}

@router.post("/orders/{order_id}/pay")
async def pay_order(order_id: int, payment_info: dict):
    """
    Pay for an order by ID.
    """
    return {"message": f"Order {order_id} paid", "payment_info": payment_info}

@router.get("/orders/{order_id}/status")
async def get_order_status(order_id: int):
    """
    Get the payment status of an order by ID.
    """
    return {"message": f"Order {order_id} payment status"}