from sqlalchemy.ext.asyncio import AsyncSession

from src.gorzdrav_api import schemas
from .abstract import AbstractRepo
from ..models import TrackingModel, UserModel


class TrackingRepo(AbstractRepo[TrackingModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model_type=TrackingModel)

    async def new(
            self,
            user: UserModel,
            district: schemas.District,
            clinic: schemas.Clinic,
            speciality: schemas.Speciality,
            doctor: schemas.Doctor,
            hours: set[int]

    ) -> TrackingModel:
        tracking = TrackingModel(
            user=user,
            district=district,
            clinic=clinic,
            speciality=speciality,
            doctor=doctor,
            hours=hours
        )
        self.session.add(tracking)

        return tracking
