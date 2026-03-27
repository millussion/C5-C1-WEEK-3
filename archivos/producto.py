
def add_product(storage):
    name = input("Name of the product: ")
    price = int(input("Price: ").replace(",","").replace(".",""))
    amount = int(input("Amount: "))

    product = {
        "name": name.strip(), 
        "price": int(price), 
        "amount": int(amount)
    }
    
    storage.append(product)
    print(f"Product {name} added correctly.")
    return name, price, amount

def show_storage(storage):

    if not storage:
        print("The inventory is empty!")
        return
    
    print("\n" + "─" * 54)
    print(f"  {'NAME':<22} {'PRICE':>10} {'AMOUNT':>10}")
    print("─" * 54)

    for product in storage:
        print(f"  {product['name']:<22} ${product['price']:>9,.0f} {product['amount']:>10}")

    print("─" * 54)
    print(f"  Total of references: {len(storage)}\n")

def search_product(storage):
    running = True
    while running:
        name = input("Name of the product: ")
        name_lower = name.strip().lower()
        for product in storage:
            if product["name"].lower() == name_lower:
                print("\n" + "─" * 54)
                print(f"  {'NAME':<22} {'PRICE':>10} {'AMOUNT':>10}")
                print("─" * 54)

                
                print(f"  {product['name']:<22} ${product['price']:>9,.0f} {product['amount']:>10}")

                print("─" * 54)
                return product
        else:
            print("Product not found. Try again.")

def upd_product(storage):

    product = search_product(storage)

    new_name = input("Enter the new name of the product: ")
    new_price = int(input("Enter the new price: ").replace(",","").replace(".",""))
    new_amount = int(input("Enter the new amount: "))
    
    
    product["name"] = new_name.strip()
    product["price"] = new_price
    product["amount"] = new_amount

    print(f"Product '{new_name}' updated.")
    return product

def delete_product(storage):
    product = search_product(storage)
    
    storage.remove(product) #.remove is a metod or a built-in function used to remove a value from a list, that's why I use "product" because what I searched in the function and stored in the variable "product" is what I'm going to remove.
    print(f"Product deleted from the storage.")
    return product

subtotal = lambda product: product["price"] * product["amount"]

def calculate_stats(storage):
    if not storage:
        return None

    # Cálculos principales usando comprensiones de lista
    units_total = sum(product["amount"] for product in storage)
    value_total      = sum(subtotal(product) for product in storage)

    # Producto con precio más alto
    max_expensive = max(storage, key=lambda product: product["price"]) #compara todos los precios de todos los productos con la función max, sin key no podriamos comparar los val
    min_expensive = min(storage, key=lambda product: product["price"]) 

    # Producto con más unidades en stock
    max_stock = max(storage, key=lambda product: product["amount"])

    return {
        "total_units":    units_total,
        "value_total":         value_total,
        "most_expensive_product":   (max_expensive["name"],    max_expensive["price"]),
        "product_less_expensive": (min_expensive["name"], min_expensive["price"]),
        "product_largest_stock":(max_stock["name"], max_stock["amount"])
    }


def show_stats(storage):
    stats = calculate_stats(storage)

    if stats is None:
        print("There is no data; the inventory is empty..")
        return

    name_expensive,   price_expensive   = stats["most_expensive_product"]
    name_minexpensive,   price_minexpensive   = stats["product_less_expensive"]
    name_stock,  amount_stock    = stats["product_largest_stock"]

    print("\n")
    print("           INVENTORY STATISTICS")
    print("═" * 44)
    print(f"  Total units in stock: {stats['total_units']:>10}")
    print(f"  Total inventory value: ${stats['value_total']:>20,.2f}")
    print(f"  Most expensive product         : {name_expensive} (${price_expensive:,.0f})")
    print(f"  Less expensive product         : {name_minexpensive} (${price_minexpensive:,.0f})")
    print(f"  Mayor stock               : {name_stock} ({amount_stock} units)")

    
    print("\n   Subtotals by product ")
    for product in storage:
        print(f"{product['name']:<22} ${subtotal(product):>10,.0f}")
    print("═" * 44 + "\n")

import csv

def save_file(storage):
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # encabezados
        writer.writerow(["name", "price", "amount"])

        # datos
        for product in storage:
            writer.writerow([
                product["name"],
                f"${product['price']:,.0f}",
                product["amount"]
            ])
            
    print("Storage saved to products.csv")

def load_file(storage):
    try:
        with open("products.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)  # saltar encabezados

            storage.clear()

            for everyrow in reader:
                name, price, amount = everyrow
                price = price.replace("$", "").replace(",", "")
                storage.append({
                    "name": name,
                    "price": int(price),
                    "amount": int(amount)
                })

        print("Storage loaded from products.csv")

    except FileNotFoundError:
        print("File not found.")