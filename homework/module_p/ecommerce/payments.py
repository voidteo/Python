from .orders import Order

class Payment:
    def __init__(self, order):
        self.order = order
    
    def pay(self):
        return f"Paid {self.order.total()}"
    