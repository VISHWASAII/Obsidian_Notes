- Like if the user add product in the cart it will be store into the cookies
- those data's are will be stored

```
response.cookie('Hello', 'World', {maxAge : 6000}); //expire after one min

clg(request.header.cookie) we can see from any endpoint
```
- we are using the cookie and we need to send to the server
- need to learn cookies and signed cookies
- we need to install the cookie parser
- It is a middleware
- import cookieParser from "cookie-Parser"
- Register to the middleware
```
app.get('/', (req, res) => {

    res.cookie('Hello', 'world', {message: "working fine"});

    res.send({message: "working fine"});

}) // we can set the time also
```

#Cookie-Parser
- It will parse our cookies
- Cookie Parser also a middleware
```
app.use(cookieParser())
```
- we can use the signed and unsigned cookies
![[Pasted image 20250402104152.png]] 
- we can also use the signed cookies
