from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.databases.database import Base, engine
from app.routers import (
    user_router, owner_router, store_router, rider_router, customer_router,
    favorite_router, review_router, payment_router, coupon_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(owner_router)
app.include_router(store_router)
app.include_router(rider_router)
app.include_router(customer_router)
app.include_router(favorite_router)
app.include_router(review_router)
app.include_router(payment_router)
app.include_router(coupon_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)
