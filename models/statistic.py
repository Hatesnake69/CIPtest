import datetime

from sqlalchemy import Column, Integer, Date, Float

from db.engine import Base


class Statistic(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    created_at = Column(Date, default=datetime.datetime.now())
    views = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    cost = Column(Float(precision=2), default=0)
    cost_per_click = Column(Float(precision=2), default=0)
    cost_per_view = Column(Float(precision=2), default=0)
