- We need to create Auth.py
- Here the Model and the Basemodel or shema is diff thats why we are just mapping it

```

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True)

    username = Column(String, unique=True)

    first_name = Column(String)

    last_name = Column(String)

    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)

    role = Column(String)


@router.post("/auth/")

async def create_user(create_user: CreateUserRequest):

    create_user_mode = Users(

        email = create_user.email,

        username = create_user.username,

        first_name = create_user.first_name,

        last_name = create_user.last_name,

        role = create_user.role,

        hashed_password = create_user.password,

        is_active = True

    )
```

- For Hashing the Password
- using bcrypt we are going to hash the password and we are going to authenticate 
```
pip install passlib
pip install bcrypt==4.0.1


from passlib.context import CryptContext

router = APIRouter()

  

bcypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

  

class CreateUserRequest(BaseModel):

    username: str

    email: str

    first_name: str

    last_name: str

    password: str

    role: str


router.post("/auth/")

async def create_user(create_user: CreateUserRequest):

    create_user_model = Users(

        email = create_user.email,

        username = create_user.username,

        first_name = create_user.first_name,

        last_name = create_user.last_name,

        role = create_user.role,

        hashed_password = bcrypt_context.hash(create_user.password)

        is_active = True

  

    )

  

    return create_user_model


```
 - This is how it is stored into the database
 ```
   

@router.post("/auth/", status_code=status.HTTP_201_CREATED)

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
```