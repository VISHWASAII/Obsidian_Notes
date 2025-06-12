- what is method in java?
```
method is a block ofcode used to perform certain task which is also known as fucntion and you can pass data into method it is called parameter
```
- How it is declared ?
```
which as access specifier - return type - method name - method argument
```
- what is polymorphism in java?
```
polymorphism is one of the four piller in java. meanning of poly many form. which allows the same method or object to behave differently based on the context.

There are two types of polymorphism one is 
method overloded another one is method override

- compile time| static poly | method overlo
- Runtime | dynamic poly | method override
```
- what is Access Specifiers?
```
Access specifiers, also known as access modifiers, are keywords in Java that control the visibility and accessibility of classes, methods, and variables.

- There are four types of access modifier
- one - public - Accessible from any class, regardless of package.
- two - private -  Accessible only within the class in which it is declared.
-three - protected - Accessible within the same package and by subclasses in other packages.
- four - default - access without same package
```
- Types of Methods?
```
there are 7 type of methods which is 
- System defined = methods which is packed with the programming language

- user defined = block of is written by a programmer

- overloaded method
- overrided method

- static method =  static method is a method associated with the class itself rather than with any specific instance (object) of that class

- final method = `final` method is a method that cannot be overridden by its subclasses

- Abstract method = An abstract method in Java is a method declared without an implementation.

```

- what is method overloaded?
```
- Method overloading in java multiple methods within the same class share the same name but have different parameter lists

- The parameter lists can differs no.of.parameters, datatype of the para, the order of the parameters

- The compiler determines which method to be invoke according to the parameter

- so it is called compile time polymorphism
```

- what is method overriding 
```
- Method overriding occurs when the subclass provides specific imp for a method which is already defined in the superclass

- the method signature [name and the parameter list] must be same and annotated with @Override parameter

- it is called run time polymorphism
```
- Variable argument
```
variable arguments which takes any no of input in the parameter
```

**Constructors:**
- what is contructors?
```
A constructor is a special method used to initialize an object when it is created. It has the same name as the class and doesn't have a return type (not even `void`). Constructors are automatically called when a new object of the class is instantiated. They are crucial for setting initial values to the object's attributes and ensuring the object is in a valid state.

- new keyword tells java to call constructors
```
- why constructor name is same as of class name?
```
constructors name is always same as class name becoz it is easy to idenfy and there is no return type becoz it implicitly java returns the instance of the class
```
- why constructor cannot be final?
```
constructors are diff from usual methods cannot be inherited so it doesn't make sense to make final becoz final used to prevent override if constructor cannot be inherited then there is no req for final 
```
- why constructor cannot be abstract?
```
since for abstract method, the responsibility of imp of child class. but constructors cant even be inherited so no point of making the abstract
```
- why we define constructor interface 
```
no becoz we cannot create object so no point of constructor
```
- Types of constructors
```
There are 5 types of constructors

1 - Default constructors
java internally provide a constructors which is known as default constructors.it will set default values for all the instance of variables

2 - No argument constructors
A constructors doesnt take any argument. similar to default constructor but we are defining instead of java

3 - Parameterized constructors
It will take one or more argument when creating an object. these parameters allow the programmer to initialize an object with specific value 

4 - constructor overloding
we can create multiple constructors with diff parameters

5 - private constructor
we can create private constructor no one outside the class will able to call the constructor. this is used usally in singleton design pattern. so to access this we need to create another static method to access this and then we can access through the method
```
- This keyword and super keyword:
```
this() - used to initialize and call or chaining the constructors

super() - is used to override the previous value of the constructor
```