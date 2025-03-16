from product_manager import ProductManager
from product import Product

# Kreiranje instanci ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 80000, 5))
manager.add_product(Product("Telefon", 40000, 10))
manager.add_product(Product("Monitor", 20000, 7))

# Prikaz proizvoda
print("Lista proizvoda:")
manager.display_products()

# Prikaz ukupne vrednosti inventara
print(f"\nUkupna vrednost inventara: {manager.total_inventory_value()} RSD")

from cart import Cart 

#Kreiranje instancu Cart
cart = Cart()

#Dodajte proizvode u korpu 
cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

#Ispis ukupne vrednosti i proizvoda u korpi
cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.total_cart_value()} RSD")


