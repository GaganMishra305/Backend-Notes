# High Level Backend Understanding

Browser --> DNS-server --> AWS-server --> AWS-firewall --> AWS-instance --> Nginx(reverse proxy) --> localhost:3000

## 1. Why cant we write backend in frontend?
- Security of code
- We cant call external apis (due to cors policy)
- Databases
- computing power


## 2. What is reverse proxy?
- A reverse proxy is a server that sits in front of one or more web servers, intercepting client requests and forwarding them to the correct backend server, then returning the server's response to the clien.
- So that we dont have to change config files again and again


## 3. What are the power of learning backend from first principles?
- seeing the big picture
- faster onboarding
- 10x faster in new projects
- syntax fatigue
- choosing right tool for right job

