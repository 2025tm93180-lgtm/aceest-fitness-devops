from flask import Flask, jsonify, request

app = Flask(__name__)

clients = []


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients)


@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "name" not in data:
        return jsonify({"error": "Client name is required"}), 400

    client = {
        "id": len(clients) + 1,
        "name": data["name"],
        "age": data.get("age"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "program": data.get("program", "Beginner"),
        "membership_status": data.get("membership_status", "Active")
    }

    clients.append(client)

    return jsonify(client), 201


@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = next(
        (client for client in clients if client["id"] == client_id),
        None
    )

    if client is None:
        return jsonify({"error": "Client not found"}), 404

    return jsonify(client)


@app.route("/programs", methods=["GET"])
def get_programs():
    programs = {
        "Fat Loss": [
            "Full Body HIIT",
            "Circuit Training",
            "Cardio + Weights"
        ],
        "Muscle Gain": [
            "Push/Pull/Legs",
            "Upper/Lower Split",
            "Full Body Strength"
        ],
        "Beginner": [
            "Full Body 3x/week",
            "Light Strength + Mobility"
        ]
    }

    return jsonify(programs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
