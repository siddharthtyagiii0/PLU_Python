import sqlite3

class Product:

    def __init__(self, product_id, product_name, category, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price

    def display(self):
        print("-----------------------------------")
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Category     :", self.category)
        print("Quantity     :", self.quantity)
        print("Price        :", self.price)

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL
)
""")

products_data = [
    (101, "Laptop", "Electronics", 15, 75000),
    (102, "Mouse", "Electronics", 8, 500),
    (103, "Keyboard", "Electronics", 20, 1200),
    (104, "Monitor", "Electronics", 6, 12000),
    (105, "Chair", "Furniture", 30, 4500),
    (106, "Table", "Furniture", 4, 7000),
    (107, "Pen", "Stationery", 100, 20),
    (108, "Notebook", "Stationery", 9, 80)
]

cursor.executemany(
    "INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?, ?)",
    products_data
)

conn.commit()

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

products = []

for row in rows:
    product = Product(row[0], row[1], row[2], row[3], row[4])
    products.append(product)

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].quantity < right[j].quantity:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

products = merge_sort(products)

print("\n========== PRODUCTS SORTED BY QUANTITY ==========\n")

for p in products:
    p.display()

products.sort(key=lambda x: x.product_id)

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid].product_id == target:
            return arr[mid]

        elif arr[mid].product_id < target:
            low = mid + 1

        else:
            high = mid - 1

    return None

print("\n========== SEARCH PRODUCT ==========")

search_id = int(input("Enter Product ID : "))

product = binary_search(products, search_id)

if product:
    print("\nProduct Found")
    product.display()
else:
    print("Product Not Found")

print("\n========== LOW STOCK PRODUCTS (Quantity < 10) ==========\n")

found = False

for p in products:
    if p.quantity < 10:
        p.display()
        found = True

if not found:
    print("No low stock products.")

conn.close()