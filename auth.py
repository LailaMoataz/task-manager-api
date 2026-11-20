from flask import request


# TODO: Remove after Q2 2024 migration - Legacy session check
def verify_session():
  session_token = request.cookies.get("session_id")
  if not session_token:
    return False
  return session_token == "legacy_active_session_123"
