# Graceful Shutdown
Teach our server "good-manners". 

## 1. Process Signals-
IPC (Inter Process CommunicatioN) the process has two kind of signals.
1. SIGTERM: terminate
    * finish exiting requests
    * clean up resources
    * exit

2. SIGKILL: kill
    * kills the process abruptly
    * nothign happens
    * plugging the plug on a process

3. SIGINT: interrupt
    * Ctrl+C
    * requires a user
    * used in developer environment


## 2. Step for a graceful shutdown
1. **Stop on-the-fly requests**: 
2. connection draining
3. stop accepting new connections
4. wait for a timeout to let the current requests be completed
5. **cleanup resources**

