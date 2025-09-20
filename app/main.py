from fastapi import FastAPI
from app.routers import posts

app = FastAPI()


# routes to pages
app.include_router(posts.post_router)


@app.get("/")
async def root():
    return {"message": "Welcome to posts API"}
