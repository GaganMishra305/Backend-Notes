# Configuration-management
SETTINGS: 
- it decides how our app runs in different environments.
- how the application starts up
- what are the diffrenet roles, features etc 
- ESSENTIALLY BEHAVIORS OF OUR API

Config management is important as our backends run on "Distributed Systems". If not done carefully then we can go into "config-chaos".

## 1. Types of Configurations
1. **Applications settings**
    - log-level: what is the log amount (DEBUG, INFO, etc)
    - port: (8080 etc)
    - connection-pool site
    - timeout values: (when to timeout an external app)

2. **Database Config**
    - host of db
    - port of db
    - user of db
    - password of db
    - name of db

3. **External Services**
    - api-keys
    - ex. clerk, stripe, ...

4. **Feature Flags**
    - for dynamically enabling or disabling features

5. **Infra config**
6. **Security config**
7. **Performance config**
8. **Business config**



## 2. Storage of Configs
1. environment-variables
2. files
    + json
    + yaml (has support for comments)
    + toml
3. key-value stores
    + redis, consul, etcd ...
4. cloud provides (for distributed environments)
    + hashicorp
    + aws-param store

## 3. Different type of enviroments for our configs
1. Dev
2. Test
3. Staging
4. Product

## 4. Secuirty configs
1. Never hardcore your secrets
2. Use some cloud based config vault; as they are encrypted and secured
3. access control for the config (following least-privilege rule)