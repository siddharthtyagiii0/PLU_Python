import sqlite3
from collections import deque

conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurant(
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    area TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Delivery(
    delivery_id INTEGER PRIMARY KEY,
    area TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    order_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    delivery_id INTEGER,
    status TEXT
)
""")

cursor.execute("DELETE FROM Restaurant")
cursor.execute("DELETE FROM Delivery")
cursor.execute("DELETE FROM Orders")

restaurants = [
    (1, "Dominos", "A"),
    (2, "Pizza Hut", "B"),
    (3, "Burger King", "C")
]

deliveries = [
    (1, "D"),
    (2, "E"),
    (3, "F")
]

orders = [
    (101, 1, 1, "Pending"),
    (102, 2, 2, "Pending"),
    (103, 3, 3, "Pending")
]

cursor.executemany("INSERT INTO Restaurant VALUES (?, ?, ?)", restaurants)
cursor.executemany("INSERT INTO Delivery VALUES (?, ?)", deliveries)
cursor.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?)", orders)

conn.commit()

print("\n========== PENDING ORDERS ==========\n")

cursor.execute("""
SELECT Orders.order_id,
Restaurant.restaurant_name,
Restaurant.area,
Delivery.area,
Orders.status
FROM Orders
INNER JOIN Restaurant
ON Orders.restaurant_id = Restaurant.restaurant_id
INNER JOIN Delivery
ON Orders.delivery_id = Delivery.delivery_id
WHERE Orders.status='Pending'
""")

pending_orders = cursor.fetchall()

for order in pending_orders:
    print(order)

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

def bfs(graph, start, goal):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbour in graph[node]:
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append(new_path)

    return None

print("\n========== SHORTEST DELIVERY PATH ==========\n")

path = bfs(graph, "A", "F")

if path:
    print(" -> ".join(path))
else:
    print("No Path Found")

print("\n========== DELIVERY ORDER SEQUENCE ==========\n")

for order in pending_orders:
    print(f"Order {order[0]} : {order[1]} ({order[2]}) -> Delivery Area {order[3]}")

order_id = int(input("\nEnter Order ID to Deliver: "))

cursor.execute("""
UPDATE Orders
SET status='Delivered'
WHERE order_id=?
""", (order_id,))

conn.commit()

print("\nOrder Delivered Successfully!")

print("\n========== UPDATED ORDERS ==========\n")

cursor.execute("SELECT * FROM Orders")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()