from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.user}:{settings.password}@"
    f"{settings.host}:{settings.port}/"
    f"{settings.name}"
)

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
