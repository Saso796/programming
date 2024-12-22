class Item :
    def __init__(self , name , price):
        self.name = name 
        self.price = price
        
class Order:
    def __init__(self , order_id , items):
        self.order_id = order_id
        self.items = items
        
    def calculate_total (self):
        total = sum (item.price for item in self.items)
        return total
    
my_orders = [Item('shampoo',350), Item('conditioner', 500) , Item('mask', 550)]
o1 = Order(71, my_orders)
print(o1.calculate_total())