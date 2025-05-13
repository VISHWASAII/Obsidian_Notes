- The previous decoder using that we are getting the user name and password in the Auth.py file 
- now we are importing that data and used for that for the CRUD
```
from .auth import get_current_user

user_dependency = Annotated[dict, Depends(get_current_user)]

//Doing dependency injection and passing the data

@router.post("/todos", status_code=status.HTTP_201_CREATED)

async def create_todo(db: db_dependency, todo_request: TodoRequest,

                      user: user_dependency):

    if user is None:

        raise HTTPException(status_code=401, detail='Authentication Failed')

    todo_model = Todos(**todo_request.dict(), owner_id=user.get('id'))

    db.add(todo_model)

    db.commit()

    return todo_model
```