
from flask import Flask, jsonify, request

app = Flask(__name__)

clients = []


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "version": "1.1.0",
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
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A valid JSON object is required"
        }), 400

    name = data.get("name")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "Client name is required"
        }), 400

    age = data.get("age")
    height = data.get("height")
    weight = data.get("weight")

    if age is not None:
        if type(age) is not int or age <= 0:
            return jsonify({
                "error": "Age must be a positive integer"
            }), 400

    for field, value in [
        ("height", height),
        ("weight", weight)
    ]:
        if value is not None:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or value <= 0
            ):
                return jsonify({
                    "error": f"{field.capitalize()} must be a positive number"
                }), 400

    client = {
        "id": len(clients) + 1,
        "name": name.strip(),
        "age": age,
        "height": height,
        "weight": weight,
        "program": data.get("program", "Beginner"),
        "membership_status": data.get(
            "membership_status", "Active"
        )
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
        return jsonify({
            "error": "Client not found"
        }), 404

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

