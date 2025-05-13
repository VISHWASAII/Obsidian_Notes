```
from fastapi import FastAPI, APIRouter, Depends, HTTPException

from pydantic import BaseModel

from models import Users

from database import SessionLocal

from typing_extensions import Annotated

from sqlalchemy.orm import Session

from starlette import status

from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from jose import jwt, JWTError

from datetime import timedelta

from datetime import datetime, timezone

  
  

router = APIRouter(

    prefix='/auth',

    tags=['auth']

)

  

SECRET_KEY = 'ADSFOIJPWfojiajfiewa83748fc9567cf3my548784395uhodf845'

ALGORITHM = 'HS256'

  

#It caries the url which client sends check token is dependency

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

  

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

  

class CreateUserRequest(BaseModel):

    username: str

    email: str

    first_name: str

    last_name: str

    password: str

    role: str

  

class Token(BaseModel):

    access_token: str

    token_type:str

  
  
  

#we are fetching the data by opening the db and close the connection

def get_db():

    db = SessionLocal()

    try:

       yield db

    finally:

        db.close()

  

db_dependency =  Annotated[Session, Depends(get_db)]

  
  

def authenticate_user(username: str, password: str, db):

    user = db.query(Users).filter(Users.username == username).first()

    if not user:

        return False

    if not bcrypt_context.verify(password, user.hashed_password):

        return False

    return user

  

def create_access_token(username: str, user_id: int, expires_delta: timedelta):

  

    encode = {'sub' : username, 'id': user_id}

    expires = datetime.now(timezone.utc) + expires_delta

    encode.update({'exp': expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

  

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get('sub')

        user_id: int = payload.get('id')

        if username is None or user_id is None:

            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,

                                detail='could not validate User. ')

        return {'username': username, 'id': user_id}

    except JWTError:

          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,

                                detail='could not validate User. ')

  

@router.post("/create_user/", status_code=status.HTTP_201_CREATED)

async def create_user(db: db_dependency,

                      create_user: CreateUserRequest):

    create_user_model = Users(

        email = create_user.email,

        username = create_user.username,

        first_name = create_user.first_name,

        last_name = create_user.last_name,

        role = create_user.role,

        hashed_password = bcrypt_context.hash(create_user.password),

        is_active = True

  
  

    )

  

    db.add(create_user_model)

    db.commit()

  
  

@router.post("/token/", response_model=Token)

async def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],

                    db: db_dependency ):

    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,

                                detail='could not validate User. ')

    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}
```