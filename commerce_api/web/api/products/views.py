from fastapi import APIRouter
from fastapi.param_functions import Depends

from commerce_api.db.repository.products_repository import ProductsRepository
from commerce_api.web.api.products.schemas import ProductInputDTO

router = APIRouter()


@router.post('/create')
def create_product(
    new_product_object: ProductInputDTO,
    products_repository: ProductsRepository = Depends(),
):
    new_product = products_repository.create(**new_product_object.dict())
    return new_product
