Strings in Java are objects. Therefore you need to use the `new` operator to create a new Java String object. Here is a Java String instantiation (creation) example:

```
String myString = new String("Hello World");
```

- All Methods Of String
![[Pasted image 20250305110300.png]]
![[Pasted image 20250305142657.png]]
## 🔹 **What are StringBuffer and StringBuilder?**

Both **StringBuffer** and **StringBuilder** are used to create **mutable (changeable) strings** in Java.

Normally, strings created with `String` are **immutable** (cannot be changed after creation). But with these two classes, you can modify the string without creating new objects every time.

---

## 🔸 **Basic difference:**

|Feature|StringBuffer|StringBuilder|
|---|---|---|
|Thread Safe|✅ Yes (synchronized)|❌ No (not synchronized)|
|Performance|Slower|Faster|
|Introduced in|Java 1.0|Java 1.5|
|Usage|When multiple threads are involved|When only one thread is involved|
- Both the buffer and builder are same the methods of string builder

|Method|Description|
|---|---|

|   |   |
|---|---|
|`append()`|Add text to the end|

|   |   |
|---|---|
|`insert()`|Insert text at a position|

|   |   |
|---|---|
|`replace()`|Replace part of the string|

|   |   |
|---|---|
|`delete()`|Delete part of the string|

|   |   |
|---|---|
|`deleteCharAt()`|Delete one character|

|   |   |
|---|---|
|`reverse()`|Reverse the string|

|   |   |
|---|---|
|`length()`|Get length of the string|

|   |   |
|---|---|
|`capacity()`|Get internal buffer size|

|   |   |
|---|---|
|`charAt()`|Get character at index|

|   |   |
|---|---|
|`setCharAt()`|Change character at index|

|   |   |
|---|---|
|`substring()`|Get part of the string|