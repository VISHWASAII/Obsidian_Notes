- There are Four type of Scopes
```
- Singleton
- prototype
- Request
- Session
```
- what is singleton scope?
```
- Defaule scope
- Only 1 instance created per IOC
- Eagerly Initialized
```
- what is prototype scope?
```
- Each time new object created
- it is lazily Initialized
- which means every time bean require it will created
```
- what is Request scope?
```
- new object created for each HTTP request
- Lazily initialized
```
- what is session scope?
```
- New object is created for each HTTP session
- Lazialy initialized
- until the session is there it will be bean will be created
```
