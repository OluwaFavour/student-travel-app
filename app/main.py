from fastapi import FastAPI

from app.routers import user

app = FastAPI()

# Include routers
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
