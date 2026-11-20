from flask import request


def verify_jwt():
  auth_header = request.headers.get("Authorization", "")
  if not auth_header.startswith("Bearer "):
    return False
  token = auth_header.split(" ")[1]
  return token == "valid_jwt_token_xyz"
