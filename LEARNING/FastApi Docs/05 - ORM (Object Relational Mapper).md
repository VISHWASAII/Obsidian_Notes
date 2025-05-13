- Layer of Abstration sits btw the db and view
- We can perform all database operations
- We dont need to create the db in the postgres
- We just define the table using the schema
- we can create filter we can do anything using the ORM
```
Sql Alchemy is the best Libaray 
```
- [I need to do the Pip Freeze]
- This is the default code to connect to the database
- And we need to connect and reuse it is default one
```
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

  
  

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/FastApi"

  

engine = create_engine(SQLALCHEMY_DATABASE_URL)

  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

  

Base = declarative_base()
```
- 