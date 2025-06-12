- used to mark method that should run asynchronously
- Runs in a new thread without blocking the main thread
- it will create a bean for that also
- if we call this method it should be the new thread
```
userServiceObj.asyncMethod()
```
- every time it will create a new thread 
- how it will create new thread?
```
it uses simpleAsyncTaskExecutor which creates new thread every time
```
- it will use default thread pool executor
- it will create default thread pool executor when nothing is there
- ThreadPoolTaskExecutor - which used to create threadpoolexcecutor
- it is hight latency to overcome this thing we need to create our own thread pool executor
```
if we created our own thread pool exec then we need to use this

@Async("myThreadPool")

and we need to use that name int he custome threadPoolExecutor
```
- The rules of Async annotation
```
- 1) The async annotated is applied to the method in a class will not work if we invoke and use the async
- No same class async method invoked

- 2) There is no interaction with the transaction and the Async. it error occur it will not roll back
- becoz it will run as sperate threat parent thread will not carry forward
```
- To overcome this we are going to use the seperate thread for transaction
```
- if we use this main thread will be free industry standard
controller -> Async -> transactional
```
- Async method return type
```
- it will return the completable feture method
- Exceptional Handler --  we need to use the AsyncUncaughtExceptionHandler
- We can customize our own expectional handler
```