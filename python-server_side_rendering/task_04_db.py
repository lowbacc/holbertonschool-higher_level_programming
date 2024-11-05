#!/usr/bin/python3

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def fetch_data_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    if source == 'json':
        # Fetch data from JSON (implement this if not already done)
        pass
    elif source == 'csv':
        # Fetch data from CSV (implement this if not already done)
        pass
    elif source == 'sql':
        products = fetch_data_from_sqlite()
        if products is None:
            return "Database error occurred", 500
        return render_template('product_display.html', products=products)
    else:
        return "Wrong source", 400

if __name__ == '__main__':
    app.run(debug=True)