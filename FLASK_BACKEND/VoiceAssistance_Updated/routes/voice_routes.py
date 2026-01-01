from flask import request, jsonify, session
import json

from VoiceAssistance_Updated.voice_blueprint import voiceBlueprint
from VoiceAssistance_Updated.agent.agent import run_agent, clear_agent_memory
from VoiceAssistance_Updated.utils.tts import speak
from VoiceAssistance_Updated.utils.validators import validate_user_text


@voiceBlueprint.route("/", methods=["POST"])
def voice_input():
    """
    Main voice/text interaction endpoint.

    Flow:
    1. Validate user input
    2. Run agent (intent → logic → response)
    3. Speak response
    4. Return intent + response
    """
    try:
        # Accept both form-data and JSON
        user_text = request.form.get("text")
        if user_text is None and request.is_json:
            user_text = request.json.get("text")

        user_text = validate_user_text(user_text)

        # 🔥 Run orchestrator (returns JSON string)
        raw_result = run_agent(user_text)
        print("Agent raw result:", raw_result)

        # Parse result safely
        try:
            parsed = json.loads(raw_result)
            intent = parsed.get("intent", "unknown")
            response_text = parsed.get("response", raw_result)
        except Exception:
            intent = "unknown"
            response_text = raw_result

        # 🔊 Speak response
        speak(response_text)

        return jsonify({
            "status": "success",
            "intent": intent,
            "response": response_text
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@voiceBlueprint.route("/welcome", methods=["POST"])
def welcome():
    """
    Welcome endpoint.
    Clears previous conversation and greets the user.
    """
    try:
        # Optional user info (name, etc.)
        user_info = request.form.get("user_info") or (
            request.json.get("user_info") if request.is_json else None
        )

        session["user_info"] = user_info

        # Clear previous conversation
        clear_agent_memory()

        welcome_text = "Welcome! What would you like to order today?"

        speak(welcome_text)

        return jsonify({
            "status": "success",
            "intent": "welcome",
            "response": welcome_text
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@voiceBlueprint.route("/clear", methods=["POST"])
def clear():
    """
    Clears entire conversation state:
    - LLM memory
    - Flask session
    """
    try:
        clear_agent_memory()
        session.clear()

        response_text = "I’ve cleared everything, let’s start fresh."

        # speak(response_text)

        return jsonify({
            "status": "success",
            "intent": "clear",
            "response": response_text
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
