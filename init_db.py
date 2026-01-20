import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/air_quality.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS classroom_air_quality (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_name TEXT,
    co2_ppm INTEGER,
    temperature REAL,
    measured_at TEXT
)
""")

cursor.executemany("""
INSERT INTO classroom_air_quality (room_name, co2_ppm, temperature, measured_at)
VALUES (?, ?, ?, datetime('now'))
""", [
    ("Lab Komputer 1", 820, 24.5),
    ("Ruang Kelas A", 950, 26.1),
    ("Ruang Kelas B", 700, 23.9)
])

conn.commit()
conn.close()

print("Database air_quality.db berhasil dibuat")
