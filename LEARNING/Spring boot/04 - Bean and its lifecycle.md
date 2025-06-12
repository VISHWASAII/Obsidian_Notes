- what is bean?
```
- Bean is a java object which is managed by Spring IOC container 
- IOC Container it will create and manage the bean
- How the bean will be created [@Component and @Bean]
- All annotated things we called bean
```
- what is @Component Annotation
```
- @Component Annotation follow Convention over configuration approach
- Spirng boot will auto configured based on conventions reducting the need of Explicit configuration
- @Controller and @Service all are internally tells spring to create bean and configure it
```
- Real time example?
```
- **`@Configuration`** = The **recipe book** 📘 that holds all the instructions (methods) for making things.
    
- **`@Bean`** = A **specific recipe** 📄 inside that book — a method that tells Spring **how to make one object (bean)**.
```
- Example Spring security?
```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    // You’re saying: "Hey Spring, I’m setting up custom security rules here."
}

@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```
- How controller and service tells spring to create bean 
```
The @Controller and the @service internally calls Spring to create bean and manage it.
```
- What all are the Annotation spring boot scanning?
```
Automatically scan and detect any class annotated with `@Component`, `@Service`, `@Repository`, or `@Controller`.

- without controller, service, repo if we want to use the Object then we are going to use the component
```
- When the Bean will be created 
```
it has two type to create a bean 
- Eagerness  -  bean has been created app started singleton scope
- Lazy  - bean will created when it needed
```
- Lifecycle of Bean:
![[Pasted image 20250602115313.png]]

```
Steps:

- During the application startup spring boot invokes IOC container
- IOC Container maked use of Configuration and @ComponentScan to look out for the classes for which beans need to be created
- Inject the dep into contructed bean using Autowired first look for bean req type. if found it will inject it.
- There are diff type of injection
- Constructor, Setter and Field.

we are use any task before and after bean creation
- @PostConstructor
- @PreDestroy
- Once the spring boot applcation stops all bean managed by the spring boot will get destroyed
```