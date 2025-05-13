- This is how Header look like
```
content-Type:application/json
```
- Content Type
```
This will provide what type of output server need to send

example

For json:
content-Type:application/json

For HTML:
content-Type: text/html; charset=UTF-8
```
- cache-control
```
We can all cache the endpoint for serveral minutes for specific endpoint
```
- Set-Cookie
```
Cookie is small piece of data send by the server to client browser

The browser stores the cookie and send each and every subsequent request
```
- Authorization Header [Bearer]
```
These header will store the Tokens

example:
Bearer Token
```
- Cross-origin resource Sharing(CORS)
```
Ensure which domain need to access the resources

it will restrict the domains
```
- X-Frame-Options
```
X-Frame-Options: DENY

This is protect from ClickJacking Attacks
```

- Headers needed while creating an application
### ✅ **Must Include (essential for almost all web apps)**

|Header|Reason|
|---|---|
|`Content-Type`|Always needed when sending/receiving JSON or HTML.|
|`Access-Control-Allow-Origin`|Needed if your frontend and backend are on different domains/ports (CORS).|
|`Authorization`|Required for protected APIs using JWT or token-based auth.|

---

### 🔐 **Strongly Recommended (for production security)**

|Header|Reason|
|---|---|
|`Strict-Transport-Security`|Enforce HTTPS and protect against downgrade attacks.|
|`X-Content-Type-Options: nosniff`|Stops browser from interpreting file types incorrectly (basic security).|
|`X-Frame-Options`|Prevents clickjacking attacks.|
|`Content-Security-Policy`|Reduces XSS risks by limiting allowed sources.|

---

### 🧁 **Optional (based on specific needs)**

|Header|When to use|
|---|---|
|`Cache-Control`|Needed only if you want to manage browser caching (like in SPAs).|
|`Set-Cookie / Cookie`|Only if you use cookies for sessions instead of tokens.|
|`Referrer-Policy`|Helpful for privacy but not critical for all apps.|