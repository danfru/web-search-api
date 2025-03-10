from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Fetch search results from DuckDuckGo API
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    data = response.json()

    results = []
    for topic in data.get("RelatedTopics", []):
        if "Text" in topic and "FirstURL" in topic:
            results.append({
                "title": topic["Text"],
                "link": topic["FirstURL"]
            })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

