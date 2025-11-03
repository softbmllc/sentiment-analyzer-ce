from flask import Flask, request, jsonify

app = Flask(__name__)

def classify(text: str) -> str:
    t = (text or "").lower()
    pos = ["good","great","excel","awesome","love","fantastic","amazing"]
    neg = ["bad","poor","terrible","awful","hate","worst","horrible"]
    if any(w in t for w in pos): return "positive"
    if any(w in t for w in neg): return "negative"
    return "neutral"

@app.get("/analyze/<path:text>")
def analyze_path(text):
    return jsonify({"label": classify(text)})

@app.get("/analyze")
def analyze_query():
    return jsonify({"label": classify(request.args.get("text",""))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
