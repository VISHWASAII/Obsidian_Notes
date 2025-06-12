```
It is project management tool which hels to - Build Generation
- Dep resolution
- Documentation
- Maven uses POM (project Object Model)
```
- Maven has step of Phases it will execute one by one as we define
![[Pasted image 20250601134436.png]]

Mvn validate
It checks for issues like missing dependencies or incorrect POM configurations.
```
./mvnw validate
```

Mvn compile
- it will validate and compile the code put it under the target and classes
```
./mvnw compile
```

Mvn test
- it will compile run and validate the testcases
```
./mvnw test
```

Mvn Package:
- it will generate the JAR or WAR file using the java
```
./mvnw package
```

Mvn verify
- it will check performance Of package
```
./mvnw verify
```

mvn install
- it used to install the dependencies of the module
```
./mvnw install
```

Mvn deploy
-  It checks for issues like missing dependencies or incorrect POM configurations.
```
./mvnw deploy
```