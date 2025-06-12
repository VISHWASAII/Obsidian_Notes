
- we are using single configuration from single configuration using @Profile annotation
- using environment Separation
```
- same code but the data configuration will be differ
- we can change the port and the url
```
- always need to use the post constructor to test the profile
```
@Value("${spring.application.name}")  
String name;  
  
@PostConstruct  
public void getValue(){  
    System.out.println(name);  
}


or else we need to use 
spring:  
  application:  
    name: Military-Asset-Management-System-dev  
  profile:  
    active: qa
it will automatically show the profile 

in the live loading we need to specify which one need to run the applcation

mvn spring-boot:run -Dspring-boot.run.profiles=prod // we can initialize dinamically 

we need to set that into pom file - Mostly pom xml is clear and mostly used in the production stage

application-dev.yml

Annotated with profile
@Profile("dev")


we can create it for specific class only matches it wil create a bean
``
