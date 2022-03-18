
class Camera:
    def __init__(self, name, make, type, description, stock_quantity, buy_price, sell_price, id = None):
        self.name = name
        self.make = make
        self.type = type
        self.description = description
        self.stock = stock_quantity
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.id = id