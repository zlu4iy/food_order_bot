from app.database.models import async_session
from app.database.models import User, Category, Soup, Garnir, Salad, SecondCourse, IndependentDish
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def get_soups(category_id):
    async with async_session() as session:
        return await session.scalars(select(Soup).where(Soup.category == category_id))

async def get_second_dishes(category_id):
    async with async_session() as session:
        return await session.scalars(select(SecondCourse).where(SecondCourse.category == category_id))

async def get_salades(category_id):
    async with async_session() as session:
        return await session.scalars(select(Salad).where(Salad.category == category_id))

async def get_garnirs(category_id):
    async with async_session() as session:
        return await session.scalars(select(Garnir).where(Garnir.category == category_id))

async def get_independent_dish(category_id):
    async with async_session() as session:
        return await session.scalars(select(IndependentDish).where(IndependentDish.category == category_id))
