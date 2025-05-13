- First i need to install the pacakge
```
pip install jose[cryptography]
pip install python-jose

from jose import jwt

  

SECRET_KEY = 'ADSFOIJPWfojiajfiewa83748fc9567cf3my548784395uhodf845'

ALGORITHM = 'HS256'




def create_access_token(username: str, user_id: int, expires_delta: timedelta):

  

    encode = {'sub' : username, 'id': user_id}

    expires = datetime.now(timezone.utc) + expires_delta

    encode.update({'exp': expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

//We are just returning the jwt token

@router.post("/token/")

async def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],

                    db: db_dependency ):

    id = 123

    user = authenticate_user(form_data.username, form_data.password, db)

    if  user:

        token = create_access_token(form_data.username, id, timedelta(minutes=20))

        return token

    return 'successfull Authentication'
```

- We need to create Schemas for the jwt and we can return it
```
The token need to be be barear token

return {'access_token': token, 'token-type':'breaer'}

This is for encoding
```

- For Decoding the jwt we are going to use one more thing
```
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


#It caries the url which client sends

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

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
```
