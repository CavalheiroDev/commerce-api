from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi.param_functions import Depends

from commerce_api.products.repository.products_repository import ProductsRepository
from commerce_api.products.schemas import (
    ProductInputDTO,
    ProductAlreadyExists,
    ProductOutputDTO,
    ProductNotExists,
)

router = APIRouter()


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_model=ProductOutputDTO,
    responses={
        201: {'model': ProductOutputDTO},
        400: {'model': ProductAlreadyExists},
    },
)
async def create_product(
    new_product_object: ProductInputDTO,
    products_repository: ProductsRepository = Depends(),
):
    new_product = await products_repository.create(data=new_product_object.dict())
    return new_product


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=List[ProductOutputDTO],
    responses={
        200: {'model': List[ProductOutputDTO]},
        400: {'model': None},
    },
)
async def list_products(
    offset: int = 0,
    limit: int = 10,
    products_repository: ProductsRepository = Depends(),
):
    products = await products_repository.get_paginated(offset=offset, limit=limit)
    return products


@router.get(
    '/{name}',
    status_code=status.HTTP_200_OK,
    response_model=ProductOutputDTO,
    responses={
        200: {'model': ProductOutputDTO},
    },
)
async def filter_by_name(
    name: str,
    products_repository: ProductsRepository = Depends(),
):
    products = await products_repository.filter(name=name)
    return products


@router.put(
    '/{product_id}',
    status_code=status.HTTP_200_OK,
    response_model=ProductOutputDTO,
    responses={
        200: {'model': ProductOutputDTO},
        400: {'model': ProductNotExists},
    },
)
async def update_product(
    product_id: str,
    new_product_object: ProductInputDTO,
    products_repository: ProductsRepository = Depends(),
):
    updated_product = await products_repository.update(
        product_id,
        **new_product_object.dict()
    )
    return updated_product
