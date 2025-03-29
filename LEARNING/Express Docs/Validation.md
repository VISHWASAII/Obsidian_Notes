- we can able to restrict the input by using the validation
```
npm i install express-validator
```

- it is also a middleware
![[Pasted image 20250327101448.png]]
 - we need to import the library and we can use it
 - it is used to validate the input request
 ![[Pasted image 20250327102134.png]]
 - Using the validatorResult we will get the list of errors
 - we can define min and max charcter
 ![[Pasted image 20250328184248.png]]
 - We can validate like this
 ![[Pasted image 20250329114401.png]]
 - we need to send the res as a array of error
 ![[Pasted image 20250329114608.png]]
- we need to check the schema using creating util folders and we need to write the schema using validator we need to import it
![[Pasted image 20250329115535.png]]
- we need to create this file in the folder of the utils
![[Pasted image 20250329115553.png]]

