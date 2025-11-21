from fastapi import FastAPI
from blog.routes import blog_route

app = FastAPI()

version = "v1.0"

app.include_router(blog_route, prefix=f"/api/{version}")
