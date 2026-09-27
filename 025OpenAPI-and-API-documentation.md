# OpenAPI Specification And Contract-First Design

## 1. Code-First vs Contract-First
- **Code-First**: Write backend controllers/handlers first, then generate Swagger/OpenAPI docs via reflection or docstring tags.
  - *Risk*: API contracts frequently drift; frontends and SDK consumers are blocked until code is merged.
- **Contract-First (Spec-First)**: Define the OpenAPI 3.1 YAML specification collaboratively first.
  - *Benefit*: Auto-generate mock servers (Prism), client SDKs (OpenAPI Generator), and server routing interfaces. Frontend and backend develop concurrently against a frozen contract.

## 2. Essential OpenAPI 3.1 Components
```yaml
openapi: 3.1.0
info:
  title: User Management Service API
  version: 1.0.0
paths:
  /users/{id}:
    get:
      summary: Retrieve user by UUID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: User profile found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        '404':
          description: User not found
```
