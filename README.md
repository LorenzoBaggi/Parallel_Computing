# Parallel_Computing
- Section 2: defined threads and processes, what they are and main differences. Java, C++, GO are different wrt Python let's say we have 4 CPUs free to execute 4 threads. when we have one thread executed by one CPU, the python interpreter will lock the remaining threads of that program. only one thread at a time is executed on any processor: it's the GIL hence there is no point of using threads to speed the program when the program is CPU bound (usually, when there are a lot of calculations to be done, like, GAMING / GRAPHING / ENCRYPTION / VIDEO AUDIO / ML ...) the opposite of a CPU bound process is a I/O process (file transfer, webpage crawler, web servers) to speed up a CPU BOUND, use multi-processes. threads run in the same memory space (different from processes) threads are lightweight, resource light process gives you more isolation in python you don't have the limitation of the GIL w/ processes with spawn it is lower to start but consumes less memory
- Section 3: MEMORY SHARING. Inter Process communication. Message passing (two threads sending messages to each other) Shared memory (two friends, instead of talking, are exchanging information looking at a "blackboard". The advantage here, wrt to message passing, is efficiency W/ threads memory sharing is helpful. Wrote a program to count the letters from multiple sites using multiple threads, but problem of thread syncronization!
- Section 4: THREAD SYNCHRONIZATION: solved the problem of the bank account using Lock(), meaning that if a variable is a shared one, while a thread acquires it the other cannot!
- Section 5: JOIN. We used join in order to wait for threads to be completed. Moreover, we protected the access of a variable through the use of Lock(). We also created a search algorithm that looks in the PC for a specific file. Then, we optimized this recursive search function thorugh multi-thread implementation
- Section 7: introduction to barriers. A barrier is a tool that allows to syncrhonize different threads / processes together. When the threads hit together the barrier, they will again start running again. Then, we made an example about Matrix Multiplication, a CPU intensive task. So, we can distribute it over multiple threads. O(n^3) Sets of barriers are useful to syncrhonize things. However, using threads incur into the pythonic problem of GIL, hence, no outperformance are found.
- Section 8: 
