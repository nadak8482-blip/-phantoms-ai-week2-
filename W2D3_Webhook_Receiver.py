from datetime import datetime
import json
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def init_db():
  with sqlite3.connect("store.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS webhook_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                received_data TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
    conn.commit()


@app.route("/webhook", methods=["POST"])
def webhook():
  if request.is_json:
    data = request.get_json()

    print("--- Received Webhook Data ---")
    print(json.dumps(data, indent=4))

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect("store.db") as conn:
      cursor = conn.cursor()
      cursor.execute(
          "INSERT INTO webhook_logs (received_data, timestamp) VALUES (?, ?)",
          (json.dumps(data), timestamp),
      )
      conn.commit()

    return jsonify({"status": "received"}), 200

  return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
  init_db()
  app.run(host="0.0.0.0", port=5000, debug=True)

