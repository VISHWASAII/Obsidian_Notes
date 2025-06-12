- How many type of memory which java Creates?
```
There are 2 types of memory which java creates. jvm manages both

1 - Stack
2 - Heap

1) Stack
Stack memomry stores temp variable and seprate memory block for the methods

- Stores primitive data types
- Stores ref of heap objects (Strong ref, weak ref, soft ref)

Each thread has own Stack

variables within scope is only visible if it goes our the it will be deleted in LIFO order

when stack memory full it through "stackoverflowError"

2)Heap Memory
- Stores objects and there is no order of allocation of memory
- Garbage Collector is used to delete un referenced object from the heap 
- it follows 'Mark and sweep algorithm'
- Types of Garbage collector - single, parallel, G1 and concurrent mark and sweep
- Heap memory is shared with all the threads
```

- Explain how this memory management works?
```
lets consider if we create a class like this

public class Main{  
    public static void main(String[] args){  
        Animals getAnimals = new Animals();  
        String animalNames = "tommy";  
        int valueOfAnimal = 10;  
    }  
}
- the primitive datatype will be stored into the stack and the object will be stored into the Head and the reference of the object will be stored into the memory
- Similarly string has the string pool which will store the value if again a string created nd uses the same name then it will use the same name
```
![[Pasted image 20250517114154.png]]

- when it stack got deleted ?
```
- As soon as we encounter the closing bracket of memory management scope ends, it will delete its scope so all the portion of the blue gets deleted
- Now again we encounterin the closing bracket which means the scope of the main ends its portion in stack deleted in LIFO order
```
- how Garbage collectors Cleared the references?
```
Stack cleared all the ref are deleted but the objects in the heap. So thats where garbage collectors work comes will deleted all unreferenced object from the heap
```
- Who controlled Garbage Collectors?
```
IT runs periodically and its controlled by the jvm. The frequency of GC running is directly proportinal to how much of the heap memory is currectly full
```
- Types of References:
```
there are three types of references
1 - strong
2 - weak
3 - soft

Strong:
- It is when variable in stack which refering an object in a heap memory
- Person pobj = new Person();
- until reference is there it wont delete

Weak Reference:
- in wek ref also ref exists to na obj in the heap but as soon as GC runs the obj get deleted from the heap memory even it is refering this obj from stack. variable will get null 

// Create a strong reference to an object  
String strongReference = new String("Hello, Weak Reference!");  
  
// Create a weak reference to the same object  
WeakReference<String> weakReference = new WeakReference<>(strongReference);

Soft References:
it will delete the reference if the storatge of heap memory. so that gc will delete it

example:
Person obj1  = new Persion();
Person obj2 = new Personn

the obj1 have a ref to the obj2 in heap, the early object was ref of obj1 will be deleted
```