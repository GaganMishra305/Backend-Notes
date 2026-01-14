# Concurrency And Parallelism
* **Concurrency**: doing multiple things at once; we use 1 core at a time; so it uses context switching; *dealing with multiple things at once* ---> I/O-bound processes
* **Parallelism**: executing mutliple instructions at the same time; we need hardware level support for this; it needs multiple core; *doing with multiple things at once* ---> CPU-bound process

## 1. How?
1. **Threads**
    - Cost overhead mmeory
    - creation memory

2. **Event loops**
    - ![event-loop](public/event-loop.png)

## 2. Backend in different concurrency model
1. Threading model
    - ![threading-model](public/threading-model.png)

2. Event loop model
    - ![eventloop-model](public/event-loop.png)

3. Virtual thread
    - ![virtuaalt text](public/virtual-threads.png )

## 3. Concurrent programs are state-machines
![state-nmachine](public/state-machine.png)

**RACE**
- ![race](public/race.png)
