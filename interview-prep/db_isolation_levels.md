# Database Isolation Levels & Anomalies
| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :--- | :--- | :--- |
| **Read Uncommitted** | Possible | Possible | Possible |
| **Read Committed** (Postgres default) | Prevented | Possible | Possible |
| **Repeatable Read** | Prevented | Prevented | Prevented in Postgres (SSI) |
| **Serializable** | Prevented | Prevented | Prevented |
