from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from commerce_api.db.dependencies import get_db_session
from commerce_api.db.models.products import Products, ProductsEntity
from utils.dao.contracts import IDAO


class ProductDAO(IDAO):
    model = Products

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, **fields) -> ProductsEntity:
        entity = self.model(**fields)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, product: ProductsEntity, **fields) -> ProductsEntity:
        for key, value in fields.items():
            setattr(product, key, value)

        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def filter(self, **fields) -> ProductsEntity:
        products = await self.session.execute(select(self.model).filter_by(**fields))
        return products.scalar()

    async def get_paginated(self, offset: int = 0, limit: int = 10) -> List[ProductsEntity]:
        products = await self.session.execute(
            select(self.model).limit(limit).offset(offset),
        )
        return products.scalars().all()
