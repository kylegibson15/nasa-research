from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.entities.analytics import Analytics
from app.infrastructure.data_access.analytics.analytics_mapper import AnalyticsMapper
from app.infrastructure.data_access.analytics.analytics_model import AnalyticsModel

class AnalyticsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_analytics_by_mission_id(self, mission_id: UUID) -> Analytics | None:
        try:
            statement = select(AnalyticsModel).where(AnalyticsModel.mission_id == mission_id)
            response = await self.session.exec(statement)
            analytics = response.first()
            return AnalyticsMapper.model_to_entity(analytics) if analytics is not None else None
        except Exception as e:
            raise Exception(f"Error while getting analytics by mission id {mission_id} - Error: {e}")

    async def create_analytics(self, analytics: Analytics) -> Analytics:
        try:
            model = AnalyticsMapper.entity_to_model(analytics)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return AnalyticsMapper.model_to_entity(model)
        except Exception as e:
            raise Exception(f"Failed creating analytics: {e}") from e