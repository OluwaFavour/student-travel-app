from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# GET /users/
@router.get("/{user_id}")
async def get_user():
    return {"message": "We are in the users route"}


# POST /users/
@router.post("/")
async def create_user():
    return {"message": "I will create a user"}