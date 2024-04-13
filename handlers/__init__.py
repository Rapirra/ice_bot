from aiogram import Router

from .pickup_handler import router as pickup_router, SubscriptionStates


router = Router(name=__name__)

router.include_routers(
    pickup_router,
)


