# online_sales_analysis

# online_sales_analysis

Ovaj projekat omogućava analizu online prodaje sa osnovnim funkcionalnostima za upravljanje proizvodima i korpom kupca.

## Klase:

### Product
- Atributi: `name`, `price`, `quantity`
- Metode:
  - `display_info()`: Prikazuje informacije o proizvodu.
  - `update_quantity(new_quantity)`: Ažurira količinu proizvoda.

### ProductManager
- Atributi: `product` (lista proizvoda)
- Metode:
  - `add_product(product)`: Dodaje proizvod u listu.
  - `display_product()`: Prikazuje sve proizvode.
  - `total_inventory_value()`: Prikazuje ukupnu vrednost inventara.

### Cart
- Atributi: `cart_items` (lista proizvoda u korpi)
- Metode:
  - `add_to_cart(product)`: Dodaje proizvod u korpu.
  - `calculate_total()`: Računa ukupnu vrednost korpe.
  - `display_cart()`: Prikazuje sadržaj korpe.

## Funkcionalnosti:
- Dodavanje proizvoda.
- Ažuriranje količine proizvoda.
- Prikaz svih proizvoda i ukupne vrednosti inventara.
- Upravljanje korpom kupca.
