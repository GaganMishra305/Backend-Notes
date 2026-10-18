# ACID vs CAP Consistency Distinction
- **Consistency in ACID**: Preserves database invariants (e.g. account balances cannot drop below zero, foreign key constraints are satisfied).
- **Consistency in CAP**: Linearizability (all clients see the exact same value for a register simultaneously as if there is only a single copy of data).
- They represent completely different concepts despite sharing the word 'Consistency'.
