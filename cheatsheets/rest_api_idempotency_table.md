# REST Method Idempotency and Safety
| HTTP Method | Safe? | Idempotent? | Expected Success Code |
| :--- | :--- | :--- | :--- |
| **GET** | Yes | Yes | 200 OK |
| **HEAD** | Yes | Yes | 200 OK |
| **OPTIONS** | Yes | Yes | 200 OK / 204 No Content |
| **POST** | No | No | 201 Created / 200 OK |
| **PUT** | No | Yes | 200 OK / 204 No Content |
| **PATCH** | No | No (usually) | 200 OK |
| **DELETE** | No | Yes | 200 OK / 204 No Content |
