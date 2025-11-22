from fastapi import FastAPI
from blog.routes import blog_route
from blog import models
from blog.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

version = "v1.0"

app.include_router(blog_route, prefix=f"/api/{version}")
