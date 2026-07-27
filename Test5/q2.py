import sqlite3
import heapq

class Patient:

    def __init__(self, patient_id, name, age, priority_level, status):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.priority_level = priority_level
        self.status = status

    def display(self):
        print("-----------------------------------")
        print("Patient ID :", self.patient_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Priority   :", self.priority_level)
        print("Status     :", self.status)

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    priority_level INTEGER,
    status TEXT
)
""")

patients_data = [
    (101, "Rahul", 45, 2, "Waiting"),
    (102, "Aman", 60, 1, "Waiting"),
    (103, "Priya", 28, 4, "Waiting"),
    (104, "Neha", 35, 3, "Waiting"),
    (105, "Rohan", 50, 5, "Waiting")
]

cursor.executemany(
    "INSERT OR REPLACE INTO patients VALUES (?, ?, ?, ?, ?)",
    patients_data
)

conn.commit()

cursor.execute("SELECT * FROM patients WHERE status='Waiting'")
rows = cursor.fetchall()

patients = []

for row in rows:
    patients.append(Patient(row[0], row[1], row[2], row[3], row[4]))

priority_queue = []

for patient in patients:
    heapq.heappush(priority_queue, (patient.priority_level, patient))

print("\n========== PATIENT ATTENDANCE ==========\n")

while priority_queue:

    priority, patient = heapq.heappop(priority_queue)

    print("Attending Patient:")
    patient.display()

    cursor.execute(
        "UPDATE patients SET status='Attended' WHERE patient_id=?",
        (patient.patient_id,)
    )

    conn.commit()

print("\n========== REMAINING WAITING PATIENTS ==========\n")

cursor.execute("SELECT * FROM patients WHERE status='Waiting'")
remaining = cursor.fetchall()

if remaining:
    for row in remaining:
        print(row)
else:
    print("No patients are waiting.")

conn.close()