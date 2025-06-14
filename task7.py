import sqlite3


conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sample_data = [
    ('Laptop', 3, 50000),
    ('Phone', 5, 20000),
    ('Tablet', 2, 15000),
    ('Laptop', 1, 50000),
    ('Phone', 3, 20000)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()



