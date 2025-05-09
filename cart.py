class Cart: 
    def __init__(self): 
        self.cart_items = []
        
    def add_to_cart(self, product):
        self.cart_items.append(product)
        
    def total_cart_value(self):
        return sum(product.price * product.quantity for product in self.cart_items)
    
    def display_cart(self):
        for item in self.cart_items:
            print(item.display_info())
            
            