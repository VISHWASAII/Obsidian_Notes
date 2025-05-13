- First we need to import the API Router then we need to add it in the router
```
from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/auth/")

async def get_user():

    return {'user': 'Authenticated'}
```

- Then we need to configure with the code
```
from Routers import auth

app.include_router(auth.router)
```