from flask import Blueprint

# Voice Assistance Blueprint
voiceBlueprint = Blueprint(
    "voice_assistance",
    __name__,
    url_prefix="/voice"
)
# --- IGNORE ---