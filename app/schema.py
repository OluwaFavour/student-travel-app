from datetime import datetime
import re
from pydantic import BaseModel, EmailStr, validator

# Username is 4-32 characters long,
# can contain letters, numbers, underscores, hyphens and dots.
# It cannot start or end with a dot, underscore or hyphen.
# It can't contain two dots, underscores or hyphens in a row.
username_pattern = re.compile(
    r"^(?=.{4,32}$)(?![_.-])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$"
)

# Password should contain at least:
# 8 characters,
# one uppercase letter,
# one lowercase letter,
# one number and
# one special character.
password_pattern = re.compile(
    r"(?P<password>((?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)(?=\S*[\!\"\§\$\%\&\/\(\)\=\?\+\*\#\'\^\°\,\;\.\:\<\>\ä\ö\ü\Ä\Ö\Ü\ß\?\|\@\~\´\`\\])\S{8,}))"
)

# Firstname and lastname should contain at least 2 characters and only letters.
name_pattern = re.compile(r"^[a-zA-Z]{2,}$")

# Phone number should contain at least 6 digits.
phone_number_pattern = re.compile(r"^\+?[0-9]{6,}$")


class UserModel(BaseModel):
    username: str
    firstname: str
    lastname: str
    middle_name: str | None
    date_of_birth: datetime
    email: EmailStr
    phone_number: str
    country_of_birth: str
    country_of_residence: str
    date_created: datetime

    @validator("username")
    async def username_validator(cls, username):
        if not username_pattern.match(username):
            raise ValueError("Username is not valid.")
        return username

    @validator("firstname", "lastname", "middle_name")
    async def name_validator(cls, v):
        if not name_pattern.match(v):
            raise ValueError("Name is not valid.")
        return v

    @validator("phone_number")
    async def phone_number_validator(cls, phone_number):
        if not phone_number_pattern.match(phone_number):
            raise ValueError("Phone number is not valid.")
        return phone_number


class UserCreate(UserModel):
    password1: str
    password2: str

    @validator("password1", "password2")
    async def password_validator(cls, password):
        if not password_pattern.match(password):
            raise ValueError("Password is not valid.")
        return password

    @validator("password2")
    async def password_match_validator(cls, password, values):
        if "password1" in values and password != values["password1"]:
            raise ValueError("Passwords do not match.")
        return password


class User(UserModel):
    id: int
    profile_picture: bytes | None

    class Config:
        orm_mode = True
