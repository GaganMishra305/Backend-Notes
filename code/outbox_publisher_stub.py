import time

class OutboxPublisher:
    def __init__(self, db_conn, kafka_producer):
        self.db = db_conn
        self.producer = kafka_producer

    def poll_and_publish(self):
        records = self.db.query("SELECT id, topic, payload FROM outbox WHERE published = FALSE LIMIT 50 FOR UPDATE SKIP LOCKED")
        for rec in records:
            self.producer.send(rec["topic"], rec["payload"])
            self.db.execute("UPDATE outbox SET published = TRUE WHERE id = %s", (rec["id"],))
