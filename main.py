import datetime

from fastapi import FastAPI, Body, Query
from dal.statistic_dal import StatisticDAL
from db.engine import async_session
from serializers.statistic import (
    CreateStatisticCommand,
    StatisticResult,
    GetStatisticFromToDateCommand,
    FilterModel,
)

app = FastAPI()


@app.post("/statistics")
async def create_statistic(
    cmd: CreateStatisticCommand = Body(
        {"views": 100, "clicks": 200, "rub_cost": 8, "cost_per_click": 10},
        examples={
            "correct": {"views": 5, "clicks": 6, "rub_cost": 8},
            "incorrect": {
                "views": "5",
                "clicks": -2,
                "rub_cost": "hello world!",
                "cost_per_click": -2,
                "cost_per_view": "tuple",
            },
        },
    )
):
    async with async_session() as session:
        async with session.begin():
            statistics_dal = StatisticDAL(session)
            new_stat = await statistics_dal.create_statistic(
                cmd=CreateStatisticCommand(
                    views=cmd.views,
                    clicks=cmd.clicks,
                    rub_cost=cmd.rub_cost,
                    cost_per_click=round(cmd.rub_cost / cmd.clicks, ndigits=2),
                    cost_per_view=round(cmd.rub_cost / cmd.views, ndigits=2),
                )
            )
            return StatisticResult(
                created_at=new_stat.created_at,
                views=new_stat.views,
                clicks=new_stat.clicks,
                rub_cost=new_stat.cost,
                cost_per_click=new_stat.cost_per_click,
                cost_per_view=new_stat.cost_per_view,
            )


@app.get("/statistics")
async def get_statistics(
    from_date: datetime.date = Query(example=datetime.date.today()),
    to_date: datetime.date = Query(example=datetime.date.today()),
    filter_column: FilterModel = Query(example="created_at"),
    desc: bool = Query(example=False),
):
    async with async_session() as session:
        async with session.begin():
            statistics_dal = StatisticDAL(session)
            statistics_list = await statistics_dal.get_statistics_from_to_date(
                cmd=GetStatisticFromToDateCommand(
                    from_date=from_date,
                    to_date=to_date,
                    filter_column=filter_column,
                    desc=desc,
                )
            )
            return [
                StatisticResult(
                    created_at=elem.created_at,
                    rub_cost=elem.cost,
                    views=elem.views,
                    clicks=elem.clicks,
                    cost_per_view=elem.cost_per_view,
                    cost_per_click=elem.cost_per_click,
                )
                for elem in statistics_list
            ]


@app.delete("/delete_all_statistics")
async def delete_all_statistics():
    async with async_session() as session:
        async with session.begin():
            statistics_dal = StatisticDAL(session)
            await statistics_dal.delete_all_statistics()
            return {"message": "All data successfully deleted"}
