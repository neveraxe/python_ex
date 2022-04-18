class Smartphone:
    def __init__(self, brand, price):
        self._brand = brand
        self._price = price
        
    def get_price(self):
        return self._price
        
    def set_price(self, price):
        self._price = price