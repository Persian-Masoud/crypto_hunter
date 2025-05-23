from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Replace with your actual activation keys ---
VALID_KEYS = {
    "2QK6X8V3": None,
    "A0DKU9QY": None,
    "GH4LB09W": None,
    # ... (add all your keys here)
}

@app.route("/activate", methods=["POST"])
def activate():
    data = request.json
    key = data.get("key")
    system_id = data.get("system_id")
    if key not in VALID_KEYS:
        return jsonify({"status": "invalid", "message": "Key not found"}), 400
    if VALID_KEYS[key] is None:
        # First use: activate and lock to this system_id
        VALID_KEYS[key] = system_id
        return jsonify({"status": "ok"})
    if VALID_KEYS[key] == system_id:
        # Already activated on this system
        return jsonify({"status": "ok"})
    # Already used on a different system
    return jsonify({"status": "used", "message": "Key already used"}), 403

@app.route("/")
def home():
    return "Activation server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
