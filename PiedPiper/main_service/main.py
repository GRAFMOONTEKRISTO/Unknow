from fastapi import FastAPI
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from redis import asyncio as aioredis
# from starlette.staticfiles import StaticFiles

from .auth.base_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate

app = FastAPI(
    title='PiedPiper'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# все подключенные роутеры
# app.include_router(router_operation)
# app.include_router(router_tasks)
# app.include_router(router_pages)


# @app.on_event("startup")
# async def startup():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
