from fastapi import FastAPI
from .routers.blog import blog_route
from .routers.user import user_route
from .blog import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

version = "v1.0"

app.include_router(blog_route, prefix=f"/api/{version}")
app.include_router(user_route, prefix=f"/api/{version}")
