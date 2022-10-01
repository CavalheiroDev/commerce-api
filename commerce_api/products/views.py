from typing import List
from uuid import UUID

from fastapi import APIRouter, status, Depends, Body

from commerce_api.products.repository.products_repository import ProductsRepository
from commerce_api.products.schemas import (
    ProductInputDTO,
    ProductAlreadyExists,
    ProductOutputDTO,
    ProductNotExists,
)
from commerce_api.products.services import ProductDbCreator

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
    new_product_object: ProductInputDTO = Body(),
    product_db_creator: ProductDbCreator = Depends(),
):
    new_product = await product_db_creator.create_product(data=new_product_object.dict())
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
    products = await products_repository.get_paginated_products(offset=offset, limit=limit)
    return products


@router.get(
    '/{product_id}',
    status_code=status.HTTP_200_OK,
    response_model=ProductOutputDTO,
    responses={
        200: {'model': ProductOutputDTO},
    },
)
async def filter_by_id(
    product_id: UUID,
    products_repository: ProductsRepository = Depends(),
):
    product = await products_repository.find_by_product_id(product_id=str(product_id))
    return product


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
    product_id: UUID,
    new_product_object: ProductInputDTO,
    products_repository: ProductsRepository = Depends(),
):
    updated_product = await products_repository.update_product(
        product_id,
        **new_product_object.dict()
    )
    return updated_product
