- This is main.py file
```
from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

import models

from models import Todos

from typing_extensions import Annotated

from database import engine, SessionLocal

  

app = FastAPI()

  

#IT all together create all the work by starting the engine

models.Base.metadata.create_all(bind=engine)

  
  

#we are fetching the data by opening the db and close the connection

def get_db():

    db = SessionLocal()

    try:

       yield db

    finally:

        db.close()

  

db_dependency =  Annotated[Session, Depends(get_db)]

  

@app.get("/")

async def read_all(db: db_dependency):

    return db.query(Todos).all()


@app.get("/todo/{todo_id}")

async def read_todo(db: db_dependency, todo_id: int):

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is not None:

        return todo_model

    raise HTTPException(status_code=404, detail='Todo not found.')
   
```

- This is database configuration
```
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

  

SQLALCHEMY_DATABASE_URL = "sqlite:///./Todo.db"

  

engine = create_engine(

    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}

)

  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

  

# Declare this BEFORE it's used elsewhere

Base = declarative_base()
```
- This is model Package
```
from database import Base

from sqlalchemy import Column, Integer, String, Boolean

  

class Todos(Base):

  

    __tablename__ = 'todos'

  

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    desciption = Column(String)

    priority = Column(Integer)

    complete = Column(Boolean, default=False)
```

- This is used for the Foreign Key
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

  

class Todos(Base):

  

    __tablename__ = 'todos'

  

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    desciption = Column(String)

    priority = Column(Integer)

    complete = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey(Users.id))
```