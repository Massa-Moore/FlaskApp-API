from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "long": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "long": -80.13},  # Changed id to 2
    {"id": 3, "campus": "DC", "lat": 38.89, "long": -77.01},   # Changed id to 3
]

@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/api/health">/api/health</a></li>
        <li><a href="/api/items">/api/items</a></li>
        <li><a href="/api/items/1">/api/items/1</a></li>
    </ul>
    """

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/items")
def get_all_items():
    return jsonify(DATA), 200

@app.route("/api/items/<int:item_id>")
def get_item_by_id(item_id):
    for item in DATA:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify({"error": "item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
