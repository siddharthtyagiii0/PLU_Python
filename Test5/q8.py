import sqlite3
from collections import deque

# -----------------------------------------
# Create Database
# -----------------------------------------
conn = sqlite3.connect("ride_booking.db")
cursor = conn.cursor()

# -----------------------------------------
# Create Tables
# -----------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Drivers(
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT,
    location TEXT,
    available TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Bookings(
    booking_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    driver_id INTEGER
)
""")

# -----------------------------------------
# Clear Old Data
# -----------------------------------------
cursor.execute("DELETE FROM Drivers")
cursor.execute("DELETE FROM Customers")
cursor.execute("DELETE FROM Bookings")

# -----------------------------------------
# Insert Sample Data
# -----------------------------------------
drivers = [
    (1, "Rahul", "A", "Yes"),
    (2, "Aman", "B", "Yes"),
    (3, "Neha", "D", "Yes"),
    (4, "Priya", "F", "No")
]

customers = [
    (101, "Rohan", "F"),
    (102, "Simran", "E")
]

bookings = [
    (1001, 101, None),
    (1002, 102, None)
]

cursor.executemany("INSERT INTO Drivers VALUES(?,?,?,?)", drivers)
cursor.executemany("INSERT INTO Customers VALUES(?,?,?)", customers)
cursor.executemany("INSERT INTO Bookings VALUES(?,?,?)", bookings)

conn.commit()

# -----------------------------------------
# Fetch Available Drivers
# -----------------------------------------
print("\n========== AVAILABLE DRIVERS ==========\n")

cursor.execute("""
SELECT * FROM Drivers
WHERE available='Yes'
""")

available_drivers = cursor.fetchall()

for driver in available_drivers:
    print(driver)

# -----------------------------------------
# Graph Representation
# -----------------------------------------
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

# -----------------------------------------
# BFS Function
# -----------------------------------------
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

# -----------------------------------------
# Customer Location
# -----------------------------------------
customer_location = input("\nEnter Customer Location (A-F): ").upper()

nearest_driver = None
shortest_path = None

for driver in available_drivers:

    path = bfs(graph, driver[2], customer_location)

    if path:

        if shortest_path is None or len(path) < len(shortest_path):
            shortest_path = path
            nearest_driver = driver

# -----------------------------------------
# Display Nearest Driver
# -----------------------------------------
print("\n========== NEAREST DRIVER ==========\n")

if nearest_driver:

    print("Driver ID :", nearest_driver[0])
    print("Driver Name :", nearest_driver[1])
    print("Location :", nearest_driver[2])

    print("\nShortest Path")
    print(" -> ".join(shortest_path))

else:
    print("No Driver Available")

# -----------------------------------------
# Assign Booking
# -----------------------------------------
booking_id = int(input("\nEnter Booking ID : "))

cursor.execute("""
UPDATE Bookings
SET driver_id=?
WHERE booking_id=?
""", (nearest_driver[0], booking_id))

# -----------------------------------------
# Update Driver Availability
# -----------------------------------------
cursor.execute("""
UPDATE Drivers
SET available='No'
WHERE driver_id=?
""", (nearest_driver[0],))

conn.commit()

print("\nBooking Assigned Successfully!")

# -----------------------------------------
# Display Booking Details using JOIN
# -----------------------------------------
print("\n========== BOOKING DETAILS ==========\n")

cursor.execute("""
SELECT Bookings.booking_id,
Customers.customer_name,
Drivers.driver_name
FROM Bookings
JOIN Customers
ON Bookings.customer_id = Customers.customer_id
JOIN Drivers
ON Bookings.driver_id = Drivers.driver_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()