- In a Java program data is kept in _variables_. Your Java program first declares the variables, then read data into them, execute operations on the variables, and then write the variables
- Each variable has a data type. The data type determines what kind of data the variable can contain, and what operations you can execute on it. For instance, a variable could be a number. Numbers can be added, subtracted, multiplied, divided etc. Or, a variable could be a string (text).

Operations
- Operations in Java are the instructions you can use to process the data in variables.

Classes + Objects
- Classes group **variables** and **operations** together in coherent modules. A class can have fields, constructors and methods (plus more, but that is not important now
- Objects are instances of classes. When you create an object, that object is of a certain class. **The class is like a template (or blueprint) telling how objects of that class should look**. When you create an object, you say "give me an object of this class".
- A field is a variable that belongs to a class or an object.
- Constructors are a special kind of method that is executed when an object of that class is created. Constructors typically initialize the objects internal fields
- Methods are groups of operations th**at carry out a certain function together. For instance, a method may add to numbers, and divide it by a third number.** Or, a method could read and write data in a database etc.

Interface
- Interfaces is a central concept in Java. An interface describes what methods a certain object should have available on it. A class can implement an interface. **When a class implements an interface, the class has to implement all the methods described in the interface.**

Java Syntax
- A Java file can contain the following elements:
```
- Package declaration
- Import statements
- Type declaration
    - Fields
    - Class initializers
    - Constructors
    - Methods
```

Types of Variables
- **Non-static field** – A variable that belongs to an object (also called an instance variable) and holds the object's internal state.
    
- **Static field** – A variable that belongs to the class (also called a class variable) and has the same value shared across all objects of the class.
    
- **Local variable** – A variable declared inside a method, accessible only within that method.
    
- **Parameter** – A variable passed to a method during a method call, accessible only within that method.


**Object Type - Important**
**A variable of an object type is also called a _reference_. The variable itself does not contain the object, but contains a _reference_ to the object.**


### 🔹 **Primitive Data Types**
- Difference between the Normal data type and object.
These are the basic, low-level data types in Java. They store simple values directly and are very efficient.

Example:

java

CopyEdit

`byte myByte; short myShort; char myChar; int myInt; long myLong; float myFloat; double myDouble;`

✅ **Key features of primitive types:**

- Faster and use less memory.
- Cannot be `null`.
- Store actual values (not references).
- No extra methods (just raw data).

---

### 🔹 **Wrapper (Object) Types**

These are **class-based objects** that wrap around primitive types, allowing them to be used as objects.

Example:

java

CopyEdit

`Byte myByte; Short myShort; Character myChar; Integer myInt; Long myLong; Float myFloat; Double myDouble; String myString;  // (Note: String is always an object, not a wrapper)`

✅ **Key features of wrapper (object) types:**

- Can be **`null`** (which means "no value").
- Slower and use more memory than primitives.
- Provide helpful **methods** (like `.compareTo()`, `.toString()`, etc.).
- Required when working with **collections** (like `ArrayList<Integer>`, not `ArrayList<int>`).
- Support **autoboxing/unboxing** (automatic conversion between primitive and object types).

---

### 🔹 **Quick comparison:**

|Feature|Primitive Type|Wrapper (Object) Type|
|---|---|---|
|Memory usage|Low|Higher|
|Performance|Fast|Slower|
|Can be `null`|❌ No|✅ Yes|
|Has methods|❌ No|✅ Yes|
|Used in collections|❌ No|✅ Yes|
### 🔹 **Byte** (`java.lang.Byte`)

java

CopyEdit

`byte b = 10; Byte myByte = Byte.valueOf(b); myByte.byteValue();      // returns byte myByte.intValue();       // returns int Byte.parseByte("10");    // converts String to byte Byte.compare(byte1, byte2); Byte.toString(b);        // returns String Byte.MAX_VALUE;          // 127 Byte.MIN_VALUE;          // -128`

---

### 🔹 **Short** (`java.lang.Short`)

java

CopyEdit

`Short.valueOf("10"); short s = myShort.shortValue(); Short.parseShort("10"); Short.compare(short1, short2); Short.MAX_VALUE;         // 32767 Short.MIN_VALUE;         // -32768`

---

### 🔹 **Character** (`java.lang.Character`)

java

CopyEdit

`Character.isLetter('A'); Character.isDigit('5'); Character.toUpperCase('a'); Character.toLowerCase('A'); Character.isWhitespace(' '); Character.getNumericValue('7');`

---

### 🔹 **Integer** (`java.lang.Integer`)

java

CopyEdit

`Integer.valueOf(100); int i = myInt.intValue(); Integer.parseInt("100"); Integer.toString(100); Integer.compare(int1, int2); Integer.sum(10, 20); Integer.MAX_VALUE;       // 2147483647 Integer.MIN_VALUE;       // -2147483648`

---

### 🔹 **Long** (`java.lang.Long`)

java

CopyEdit

`Long.valueOf(1000L); long l = myLong.longValue(); Long.parseLong("1000"); Long.toString(1000L); Long.compare(long1, long2); Long.sum(1000L, 2000L); Long.MAX_VALUE; Long.MIN_VALUE;`

---

### 🔹 **Float** (`java.lang.Float`)

java

CopyEdit

`Float.valueOf(10.5f); float f = myFloat.floatValue(); Float.parseFloat("10.5"); Float.toString(10.5f); Float.compare(float1, float2); Float.isNaN(f); Float.MAX_VALUE; Float.MIN_VALUE;`

---

### 🔹 **Double** (`java.lang.Double`)

java

CopyEdit

`Double.valueOf(20.55); double d = myDouble.doubleValue(); Double.parseDouble("20.55"); Double.toString(20.55); Double.compare(double1, double2); Double.isNaN(d); Double.MAX_VALUE; Double.MIN_VALUE;`

---

### 🔹 **String** (`java.lang.String`)

_(Just a few examples, as `String` has many methods!)_

java

CopyEdit

`String s = "Hello"; s.length(); s.charAt(0); s.toUpperCase(); s.toLowerCase(); s.substring(1, 3); s.contains("He"); s.equals("Hello"); s.replace("H", "J"); s.trim(); s.isEmpty();`