from api_v2 import verify_jwt
from auth import verify_session
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/old_api/profile")
def old_profile():
  if not verify_session():
    return jsonify({"error": "Unauthorized"}), 401
  return jsonify({"auth": "legacy_session", "user": "demo_user"})


@app.route("/api/v2/profile")
def new_profile():
  if not verify_jwt():
    return jsonify({"error": "Unauthorized"}), 401
  return jsonify({"auth": "jwt", "user": "demo_user"})


if __name__ == "__main__":
  app.run(debug=True)
