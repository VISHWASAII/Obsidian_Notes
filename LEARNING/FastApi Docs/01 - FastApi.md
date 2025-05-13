- Need to create virtual environment
```
py -3 -m venv [name]
```
- we need to understand the docs
```
pip install "fastapi[standard]"


(env) pip freeze > requirements.txt
```
- This is how we are going to use the fastapi
- We need to change the venv in the visual studio configuration also
```
from typing import Union

from fastapi import FastAPI

  

app = FastAPI()

  

@app.get("/")

async def get_user():

    return "Im the user"
```

- This how we need to start
```
uvicorn main:app --reload
```

#Post
- We need to extract data from param using Body in fastapi
```
from fastapi.params import Body

@app.post("/createUser")

async def create_User(payload: dict = Body(...)) -> dict:

    return user


//We are sending the user
@app.post("/createUser")

async def create_User(payload: dict = Body(...)) -> dict:

    return {"Book" : f"title {payload['title']} content: {payload['author']}"}
```
- With http status code we need to send the data
```
@app.post("/createUser", status_code=status.HTTP_201_CREATED)

async def create_User(new_post: Userpost) -> dict:

    post_dict = new_post.dict()

    if post_dict['id'] == None:

        post_dict['id'] = randrange(0, 100000000)

    my_post.append(post_dict)

    return {"Book" : my_post}
```

- For the document we can also use the #localhost8000/redoc
```
from typing import Optional

@app.get('/greet/')
async def greet(username:Optional[str]="User"):
   return {"message":f"Hello {username}"}
```