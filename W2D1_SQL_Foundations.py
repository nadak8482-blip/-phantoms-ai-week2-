import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
"""
)

items = [
    ("MacBook Air M2", "Electronics", 999.99),
    ("Wireless Earbuds", "Electronics", 59.50),
    ("Yoga Mat", "Sports", 20.00),
    ("Smart Watch", "Electronics", 199.99),
    ("Blender Pro", "Home Appliances", 85.00),
]

cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        """
        INSERT INTO products (name, category, price) 
        VALUES (?, ?, ?)
    """,
        items,
    )
    conn.commit()

print("--- Query 1: Electronics Products ---")
cursor.execute(
    "SELECT id, name, category, price FROM products WHERE category = ?",
    ("Electronics",),
)
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Price: ${row[3]}")

print("\n--- Query 2: Products Sorted by Price (High to Low) ---")
cursor.execute("SELECT id, name, category, price FROM products ORDER BY price DESC")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Price: ${row[3]}")

conn.close()

