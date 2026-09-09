import sqlite3
import requests


def main():
  url = "https://fakestoreapi.com/products"

  response = requests.get(url)
  print(f"Status Code: {response.status_code}")

  if response.status_code != 200:
    return

  items = response.json()
  extracted_products = []

  for item in items[:10]:
    product_data = {
        "title": item.get("title"),
        "price": item.get("price"),
        "category": item.get("category"),
    }
    extracted_products.append(product_data)

  conn = sqlite3.connect("store.db")
  cursor = conn.cursor()

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            category TEXT
        )
    """)

  for p in extracted_products:
    cursor.execute(
        "INSERT INTO products (title, price, category) VALUES (?, ?, ?)",
        (p["title"], p["price"], p["category"]),
    )

  conn.commit()

  print("\n--- Data Inserted Successfully ---\n")

  print("Query 1: Filter by category (WHERE)")
  target_category = extracted_products[0]["category"]
  cursor.execute(
      "SELECT title, price, category FROM products WHERE category = ?",
      (target_category,),
  )
  rows_where = cursor.fetchall()
  for row in rows_where:
    print(f"Title: {row[0]} | Price: {row[1]} | Category: {row[2]}")

  print("\n" + "=" * 40 + "\n")

  print("Query 2: Order by price descending (ORDER BY)")
  cursor.execute("SELECT title, price, category FROM products ORDER BY price DESC")
  rows_order = cursor.fetchall()
  for row in rows_order:
    print(f"Title: {row[0]} | Price: {row[1]} | Category: {row[2]}")

  conn.close()


if __name__ == "__main__":
  main()

