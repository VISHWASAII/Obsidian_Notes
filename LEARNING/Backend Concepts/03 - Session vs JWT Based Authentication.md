
- Session based Authentication Usually stores the value into the cookie
```
Firstly - When the user Authenticated The session will be created

Second -  Session will be stored into the Session Storage it will be mysql or redis [it will contain the User id, Session exp time]

Thirdly - the server send's a 'Session id' in the form of Cookies

Fourthly - that cookies will be stored in the Cookie Storage

Fifth - Whenever the user sends the data the cookie will also forwarded as header 

Sixth - Using the session id the session will be fetched and authenticating
Using the the Authorization will be happening
```
- Advantage
```
**Advantage:** Securely stores authentication data on the server, reducing exposure to client-side attacks like XSS.

**Disadvantage:** Doesn’t scale well in distributed systems without extra setup like sticky sessions or centralized storage.

```

JWT Based Authentication:
- The Jwt based Authentication the cookies are stored into the Cookies also
```
Firstly -- when the user Authenticated A Token will be created

Second -- The server sign JWT with the Secret key 

Thirdly - this will protect integrity of the token preventing tampering of the token

Foruthly -  the Token will be send to client browser

Fifthly -- it will be store on to the cookie storage
```