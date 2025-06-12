- it is used to validate the user 
```
from pydantic import BaseModel

class Userpost(BaseModel):

    title: str

    content: str




@app.post("/createUser")

async def create_User(new_post: Userpost) -> dict:

    print(new_post)
    print(new_post.title)

    return {"Book" :"Users"}
```

#Optional 
- The data might present or not
```
  

class Userpost(BaseModel):

    title: str

    content: str

    published: bool = True



from typing import Optional

  

class Userpost(BaseModel):

    title: str

    content: str

    published: bool = True

    rating: Optional[int] = None

//This will convert to dict
print(new_post.dict())
```

Please universe help me i need this job any job
