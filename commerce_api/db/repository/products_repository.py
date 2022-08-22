from typing import List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from commerce_api.db.dependencies import get_db_session
from commerce_api.db.models.products import Products
from commerce_api.db.repository.contracts import IRepository


class ProductsRepository(IRepository):
    model = Products

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    def create(self, **fields) -> model:
        entity = self.model(**fields)
        self.session.add(entity)
        return entity

    def update(self, **fields) -> model:
        pass

    def filter(self, **fields) -> model:
        pass

    def all(self) -> List[model]:
        pass

    def get_paginated(self) -> List[model]:
        pass
