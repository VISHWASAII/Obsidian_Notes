- it will do mail between the functions
- it will be req handler
- we can use multiple middleware like this
```
app.get('/', (req, res) => {

    console.log("hello");

}, (req, res) => {

    console.log('world');
    next();

},

(req, res) => {

    res.status(201).json({message : "Hello world"});
    next();

})

  

app.get('/getAllUsers', (req, res) => {

    res.status(201).send(listOfUsers);

})
```
- it will intercept each and every req
LOG
```
const logging middleware = req res 
clg(req method and req url)
```
- to enable to use this globally
```
app.use(Logging middleware, anfn => clg(finished log));
next();
```
- we need to pass it as arguments
```
app.post('createNewUsers/api', (req, res) => {
    const {name, position} = req.body;
    if(!name || !position){
        res.status(400).send({message : "name and position not found"});
    }
    const users = {
        id: uuidv4(),
        name,
        position
    }
    res.status(201).send(users);
})
```
JSON
- Used to handle the req in json
```
app.use(express.json)
```
OWN MID
- for each time i need to find the user id index right instead of that i can use the own middleware where i can pass the input and get the output
![[Pasted image 20250326132847.png]]
- And we need to pass this to the input of argument of the function
![[Pasted image 20250326133121.png]]
listen that function attach the index with the req so we can directly destructure and use it.