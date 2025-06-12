- what is class in java?
```
A class is a blueprint that defines variables (also called fields) and methods (functions). Using an instance of a class (called an object), we can access those variables and methods.
```

- how many types of classes:
```
Types of classes

Concreate Class
Abstract class
super and sub class
object class
Nested class
    - Inner class (Non static nested class)
    - Anonymous inner class
    - member inner class
    - Local inner class
    - Static nested class
Generic class
pojo class
enum class
final class
Sigleton class
immutabel class
wrapper class
```
- What is Concrete Class?
```

```
- What is Abstract Class?
```

```
- what is Nested Class?
```
- Static Nested class

public class OuterClass {  
  
    String userName = "vishwa";  
    int userAge = 12;  
  
    static class NestedClass{  
        public void print(){  
            System.out.println("working fine");  
        }  
    }}
public static void main(String[] args) {  
    OuterClass.NestedClass getNestedClass = new OuterClass.NestedClass();  
    getNestedClass.print();  
  
}

- Member Inner Class

public class OuterClass {  
  
    String userName = "vishwa";  
    int userAge = 12;  
  
    private static class NestedClass{  
        public void print(){  
            System.out.println("working fine");  
        }  
    }    public void display(){  
      NestedClass getNestedClass = new NestedClass();  
      getNestedClass.print();  
    }  
}
public class ClassesInJava {  
  
    public String valueOfUser(){  
        return "getTheValueOfUser";  
    }  
  
    public static void main(String[] args) {  
        OuterClass getOuterClass = new OuterClass();  
        getOuterClass.display();  
  
    }

-- Local inner class

- it works inside the block only if we invoke the class it will run perfectly
- Using the instance of the class we can access the method of it.

public class OuterClass {  
  
    String userName = "vishwa";  
    int userAge = 12;  
  
    public void display(){  
        int methodLocalVariable = 3;  
  
        class LocalInnerClass{  
            int localInnerVariable = 4;  
  
            public void print(){  
                System.out.println("Its working fine");  
            }  
        }        LocalInnerClass localObj = new LocalInnerClass();  
        localObj.print();  
    }  
}

-- Inheritance in nested class

- First we need to create Instance of class of outer class
- the using outer class we need to create new instance of two class

class InnerClassOne{  
    int innerClassValue = 12;  
}  
class InnerClassTwo extends InnerClassOne{  
    int innerclassTwoValue = innerClassValue + 12;  
  
    public void display(){  
        System.out.println(innerclassTwoValue);  
    }  
}
public static void main(String[] args) {  
  
    OuterClass getOuterClass = new OuterClass();  
    OuterClass.InnerClassTwo getInnerClassTwo =  getOuterClass.new InnerClassTwo();  
    getInnerClassTwo.display();  
  
}



```
