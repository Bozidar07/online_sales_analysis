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
