from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer

from commerce_api.db.base import Base


class Products(Base):
    __tablename__ = 'PRODUCTS'

    name = Column('NAME', String(length=200), nullable=False)  # noqa: WPS432
    price = Column('PRICE', Integer, nullable=False)
    stock_quantity = Column('STOCK_QUANTITY', Integer)
