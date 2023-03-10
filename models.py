from sqlalchemy import Column, String, Integer
from typing import Any
from fastapi_utils.camelcase import camel2snake
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """Автоматическая генерация имени таблицы"""
        return camel2snake(cls.__name__)


class TGContact(Base):
    _id = Column(Integer, primary_key=True)
    inn = Column(String)
    verified = Column(Integer)  # 0 = False / 1 = True
