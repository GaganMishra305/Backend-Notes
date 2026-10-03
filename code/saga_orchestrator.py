class OrderSagaOrchestrator:
    def __init__(self, payment_svc, inventory_svc):
        self.payment_svc = payment_svc
        self.inventory_svc = inventory_svc

    def execute_order(self, order_id, amount, items):
        if not self.payment_svc.authorize(order_id, amount):
            return False, "PAYMENT_FAILED"

        if not self.inventory_svc.reserve(items):
            self.payment_svc.refund(order_id, amount) # Compensating action
            return False, "INVENTORY_UNAVAILABLE"

        return True, "ORDER_CONFIRMED"
