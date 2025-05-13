```
pip install python-multipart

from fastapi.security import OAuth2PasswordRequestForm


def authenticate_user(username: str, password: str, db):

    user = db.query(Users).filter(Users.username == username).first()

    if not user:

        return False

    if not bcrypt_context.verify(password, user.hashed_password):

        return False

    return True



@router.post("/token/")

async def auth_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],

                    db: db_dependency ):

    return 'token'

```