from .user import router as user_router
from .owner import router as owner_router
from .store import router as store_router
from .rider import router as rider_router
from .customer import router as customer_router
from .favorite import router as favorite_router
from .review import router as review_router
from .payment import router as payment_router
from .coupon import router as coupon_router

__all__ = ["user_router", "owner_router", "store_router", "rider_router", "customer_router", 
           "favorite_router", "review_router", "payment_router", "coupon_router"]

