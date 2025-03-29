- A thread is not equal to a CPU though. Usually a single CPU will share its execution time among multiple threads, switching between executing each of the threads for a given amount of time. It is also possible to have the threads of an application be executed by different CPUs.

**Multitasking:**
Later came multitasking which meant that computers could execute multiple programs (AKA tasks or processes) at the same time. It wasn't really "at the same time" though. The single CPU was shared between the programs. The operating system would switch between the programs running, executing each of them for a little while before switching.

Along with multitasking came new challenges for software developers. Programs can no longer assume to have all the CPU time available, nor all memory or any other computer resources. A "good citizen" program should release all resources it is no longer using, so other programs can use them.

**Why Multithreading**
- There are several reasons as to why one would use multithreading in an application. Some of the most common reasons for multithreading are:

- Better utilization of a single CPU.
- Better utilization of multiple CPUs or CPU cores.
- Better user experience with regards to responsiveness.
- Better user experience with regards to fairness.
- 