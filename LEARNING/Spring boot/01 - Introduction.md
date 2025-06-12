- What is servlets
```
- Servlets is a java class which handles a client request and process it the it return the response
- The servlets handle by the servlets container
- First the req send the servelt container which deployed into the tomcat server
- using the web.xml it will route to the correct page
```
![[Pasted image 20250601132255.png]]
- what is the advantage of spring boot
```
- Removal of web.xml - and for the configuration they introduced Annotation based configuration
- Inversion of controlm- Previously Servels depends on servlet container to create object and maintain its lifecycle.IOC is mroe flexible way to manage the object dependencies and its lifecycle
- unit testing - it is easy to mock the object using spring dependency injection
```

- what is dependency injection?
```
- without the dependency injection or inversion of control we need to create Object of the class to overcame that we are using dependency injection
- when we create object of another class it will be Tighly coupled and it need to depend on the class it cannot be dynamic
- @Component - Tells spring that you have to manage this class or bean
- @Autowired - Tells spring to resolve and add this object dependencies
- {Main principle of Dependency injection to avoid creation of one object }
- To avoid creating dependent objects manually inside a class and instead provide those objects from the outside
```
- what is inversion of control?
```
- one object doesnt create another object we need to craete an object using framework or factory method and use it.
```
![[Pasted image 20250601133315.png]]
- what all are the types of dependency injection
```
Instead of a class **creating** its own dependencies using `new`, the dependencies are **injected** into the class — usually via:

- **Constructor Injection**
    
- **Setter Injection**
    
- **Field Injection** (less recommended)
```
- Spring boot which follows the Reflection to scan all the class and objects

Spring Layered Architecture
![[Pasted image 20250601133943.png]]


