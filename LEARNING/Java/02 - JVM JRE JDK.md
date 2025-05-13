- What all are three main components of java?
```
the three component of Java is [Jvm, Jre, Jdk]
```
- Why java called Platform Independent?
```
Java is platform-independent because the compiled bytecode can run on any system that has a JVM, regardless of the underlying operating system or hardware.
```
- What is JVM?
```
A Java Virtual Machine (JVM) is a virtual machine that enables computers to run Java programs.
```
- What is JVM work flow?
```
Java Program -> [Compiler] --> Bytecode -->[Jvm] --> Machine Code --> [CPU] --> output

workFlow 
Firstly, Java program which is compiled into bytecode

Secondly, Bytecode will converted into machine code 

Thirdly,  Machine code run top of the CPU and it will provide the output
```
- What is JRE?
```
JRE contains JVM and class Libraries. 
Using the JRE we can run the java program but we cannot code the program
```
- What is JDK?
```
JDK which has the programming language information
And it has the compiler {javac}
And it has debugger
```
- Why in java we have only one public class?
```
JVM is going to invoke the main method. so that class modifier need to be public

It need to be single entry point
```