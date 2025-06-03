from flask import Flask, request, jsonify, redirect
import hashlib

app = Flask(__name__)

# TODO replace with persistant memory
turls = {}


def short_hash(input_string):
    full_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return full_hash[:2]

@app.route("/encode", methods=["POST"])
def encode():
    data = request.get_json()
    name = data.get("url")
    surl = short_hash(name)
    turls[surl] = name
    print(turls)
    return jsonify({"message": f"localhost:80/{surl}"}), 200

@app.route("/<id>", methods=["GET"])
def get_route(id):
    print(id, turls)
    if id:
        return redirect(location=turls.get(id))
    return "No URL found", 404

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True,
    )
