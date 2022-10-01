from fastapi.routing import APIRouter

from commerce_api import products

api_router = APIRouter()
api_router.include_router(products.router, prefix='/products', tags=['products'])
