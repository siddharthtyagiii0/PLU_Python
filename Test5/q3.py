import sqlite3

class Transaction:

    def __init__(self, transaction_id, account_number, amount, date, transaction_type):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.date = date
        self.transaction_type = transaction_type

    def display(self):
        print("--------------------------------")
        print("Transaction ID :", self.transaction_id)
        print("Account Number :", self.account_number)
        print("Amount         :", self.amount)
        print("Date           :", self.date)
        print("Type           :", self.transaction_type)

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY,
    account_number TEXT,
    amount REAL,
    date TEXT,
    transaction_type TEXT
)
""")

transactions_data = [
    (101, "ACC1001", 5000, "2026-07-01", "Credit"),
    (102, "ACC1002", 2500, "2026-07-02", "Debit"),
    (103, "ACC1003", 12000, "2026-07-03", "Credit"),
    (104, "ACC1004", 8000, "2026-07-04", "Debit"),
    (105, "ACC1005", 15000, "2026-07-05", "Credit"),
    (106, "ACC1006", 3000, "2026-07-06", "Debit"),
    (107, "ACC1007", 10000, "2026-07-07", "Credit")
]

cursor.executemany(
    "INSERT OR REPLACE INTO transactions VALUES (?, ?, ?, ?, ?)",
    transactions_data
)

conn.commit()

cursor.execute("SELECT * FROM transactions")
rows = cursor.fetchall()

transactions = []

for row in rows:
    transactions.append(Transaction(row[0], row[1], row[2], row[3], row[4]))

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for transaction in arr[1:]:

        if transaction.amount < pivot.amount:
            left.append(transaction)
        else:
            right.append(transaction)

    return quick_sort(left) + [pivot] + quick_sort(right)

transactions = quick_sort(transactions)

print("\n========== TRANSACTIONS SORTED BY AMOUNT ==========\n")

for transaction in transactions:
    transaction.display()

transactions.sort(key=lambda x: x.transaction_id)

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid].transaction_id == target:
            return arr[mid]

        elif arr[mid].transaction_id < target:
            low = mid + 1

        else:
            high = mid - 1

    return None

print("\n========== SEARCH TRANSACTION ==========\n")

transaction_id = int(input("Enter Transaction ID: "))

transaction = binary_search(transactions, transaction_id)

if transaction:
    print("\nTransaction Found")
    transaction.display()
else:
    print("Transaction Not Found")

total_credit = 0
total_debit = 0

for transaction in transactions:

    if transaction.transaction_type == "Credit":
        total_credit += transaction.amount
    else:
        total_debit += transaction.amount

print("\n========== TOTAL AMOUNTS ==========")
print("Total Credit :", total_credit)
print("Total Debit  :", total_debit)

transactions = quick_sort(transactions)

print("\n========== TOP 5 HIGHEST TRANSACTIONS ==========\n")

top_transactions = transactions[-5:]
top_transactions.reverse()

for transaction in top_transactions:
    transaction.display()

conn.close()