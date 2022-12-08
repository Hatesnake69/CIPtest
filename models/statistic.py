import datetime

from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric
from pydantic import BaseModel

from db.engine import Base


class Statistic(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    created_at = Column(Date, default=datetime.datetime.now())
    views = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    cost = Column(Numeric(scale=2), default=0)
    cost_per_click = Column(Numeric(scale=2), default=0)
    cost_per_view = Column(Numeric(scale=2), default=0)


class CreateStatisticCommand(BaseModel):
    views: int = 0
    clicks: int = 0
    cost: float = 0
    cost_per_click: float = 0
    cost_per_view: float = 0
