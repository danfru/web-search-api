from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ ADD THIS HOMEPAGE ROUTE TO FIX "Cannot GET /"
@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = [
        {"title": "AI Research Paper 1", "link": "https://example.com/1"},
        {"title": "AI Research Paper 2", "link": "https://example.com/2"}
    ]
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

