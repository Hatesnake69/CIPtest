from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.statistic import (
    Statistic,
)
from serializers.statistic import CreateStatisticCommand, GetStatisticFromToDateCommand


class StatisticDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_statistic(self, cmd: CreateStatisticCommand) -> Statistic:
        print(cmd.rub_cost)
        new_record = Statistic(
            views=cmd.views,
            clicks=cmd.clicks,
            cost=cmd.rub_cost,
            cost_per_click=cmd.cost_per_view,
            cost_per_view=cmd.cost_per_view,
        )
        self.db_session.add(new_record)
        await self.db_session.flush()
        return new_record

    async def get_statistics_from_to_date(
        self, cmd: GetStatisticFromToDateCommand
    ) -> List[Statistic]:
        statement = (
            select(Statistic)
            .where(
                (cmd.from_date <= Statistic.created_at)
                & (Statistic.created_at <= cmd.to_date)
            )
            .order_by(
                getattr(Statistic, cmd.filter_column).desc()
                if cmd.desc
                else getattr(Statistic, cmd.filter_column)
            )
        )

        q = await self.db_session.execute(statement)
        return q.scalars().all()

    async def delete_all_statistics(self) -> None:
        await self.db_session.execute('TRUNCATE TABLE "statistics"')
