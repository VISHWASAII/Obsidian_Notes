- we might need to write our custom interceptors
- Spring boot caching,
- Spring boot logging,
- Spring boot authentication
```
- we can customize our intercepter and which endpoints it need to be invoked

```
![[Pasted image 20250604115855.png]]
- dispatcher servlet which only take care where the req need to route.
- inbetween the servlet and the Controller or servlets interceptor will work 

How to create Custom Annotation
```
public @Interfacr MyCustomeAnnotation{

}

@MyCustomAnnotation -- we can customize our own annotation
@Target - we can specify where i can use it. (method or class)
```

```
- we are create our own interceptor using the AOP 
- using AOP we can specify where and how we can do specifically after or befor it need to be invoked
```

- important
```
We can create a custom interceptor and we can create custom annotaion using annotaion we can speicfy the AOP interceptor
```

- This is the example
```
package com.example.annotations;

import java.lang.annotation.*;

@Target(ElementType.TYPE) 
@Retention(RetentionPolicy.RUNTIME)
public @interface LoggableController {
}




import com.example.annotations.LoggableController;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/test")
@LoggableController
public class TestController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello World";
    }

    @PostMapping("/submit")
    public String submit() {
        return "Submitted!";
    }
}


import jakarta.servlet.http.HttpServletRequest;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.*;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

@Aspect
@Component
public class LoggingAspect {

    @Pointcut("@within(com.example.annotations.LoggableController)")
    public void loggableClassMethods() {}

    @Before("loggableClassMethods()")
    public void logControllerInfo(JoinPoint joinPoint) {
        // Get request info
        ServletRequestAttributes attrs = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        if (attrs == null) return;

        HttpServletRequest request = attrs.getRequest();

        // Extract method, class, path, etc.
        String httpMethod = request.getMethod();
        String requestURI = request.getRequestURI();

        String className = joinPoint.getTarget().getClass().getSimpleName();
        String methodName = ((MethodSignature) joinPoint.getSignature()).getMethod().getName();

// here i need to use the logger instead of the sout



```

- what is the Filter vs interceptors?
```
Filter - it will intercept HTTP req and res before reach to the servlet

Interceptor - It will specific to spring framework and intercept Http req and res before they reach to the controller
```
![[Pasted image 20250604125833.png]]
- Before servlets the filter will come after the servlets the interceptor will come.
- what is servlets?
```
Servlet is java class accepts incoming req and it will return the response.
```
- Where we are using the Filter?
```
- in spring security we are using the Filter
- For perticular servlet we are going to use for intercepter
- when we can to intercept HTTP req and res we can use for all servlets
```
- best we can user filter for the authentication
```
Yes, you can use a **Filter** for authentication, especially for token validation before the request reaches Spring Security or controllers. ✅
```
- example how we are using the filters
```
import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.stereotype.Component;
import java.io.IOException;

@Component
public class AuthTokenFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        HttpServletRequest httpReq = (HttpServletRequest) request;
        HttpServletResponse httpRes = (HttpServletResponse) response;

        String token = httpReq.getHeader("Authorization");

        // Simple token check
        if (token != null && token.equals("my-secret-token")) {
            chain.doFilter(request, response); // continue
        } else {
            httpRes.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            httpRes.getWriter().write("Unauthorized");
        }
    }
}

```