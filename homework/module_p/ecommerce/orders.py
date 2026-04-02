from .products import Product
from .import SECRET_WORD


class Order:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity
    
    def total(self):
        return self.product.price * self.quantity
    

print(SECRET_WORD)