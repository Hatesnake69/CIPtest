import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, PositiveInt, validator


class StatisticResult(BaseModel):
    created_at: datetime.date
    views: PositiveInt
    clicks: PositiveInt
    rub_cost: float
    cost_per_click: float
    cost_per_view: float

    @validator("rub_cost", "cost_per_click", "cost_per_view")
    def result_check(cls, v):
        ...
        return round(v, 2)


class FilterModel(str, Enum):
    created_at = "created_at"
    views = "views"
    clicks = "clicks"
    rub_cost = "rub_cost"
    cost_per_click = "cost_per_click"
    cost_per_view = "cost_per_view"


class GetStatisticFromToDateCommand(BaseModel):
    from_date: datetime.date
    to_date: datetime.date
    filter_column: FilterModel
    desc: Optional[bool]


class CreateStatisticCommand(BaseModel):
    views: Optional[PositiveInt]
    clicks: Optional[PositiveInt]
    rub_cost: Optional[float]
    cost_per_click: Optional[float] = None
    cost_per_view: Optional[float] = None
