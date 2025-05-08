

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.routes import users, shop

api = FastAPI(
    title="Shop API",
    description="API for managing shop items",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations with users",
        },
        {
            "name": "products",
            "description": "Operations with products",
        },
        {
            "name": "orders",
            "description": "Operations with orders",
        },
    ],
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    default_response_class=JSONResponse
)


api.include_router(users.router)
api.include_router(shop.router)

@api.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok", "message": "API is running"}

@api.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    General exception handler.
    """
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred", "details": str(exc)},
    )


