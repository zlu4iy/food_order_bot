from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db_jora.sqlite3')      # Создаем БД

async_session = async_sessionmaker(engine)                                  # Подключаемся к БД

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    # name: Mapped[str] = mapped_column(String(25))
    # sirname: Mapped[str] = mapped_column(String(25))


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))


# class Dish(Base):
#     __tablename__ = 'dishes'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(25))
#     description: Mapped[str] = mapped_column(String(125))
#     category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Soup(Base):
    __tablename__ = 'soups'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Garnir(Base):
    __tablename__ = 'garnirs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class Salad(Base):
    __tablename__ = 'salades'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(125))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class SecondCourse(Base):
    __tablename__ = 'second_courses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


class IndependentDish(Base):
    __tablename__ = 'independent_dishes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
