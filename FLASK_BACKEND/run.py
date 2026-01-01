from flask import Flask
from app import create_app
from model import model_blueprint

from VoiceAssistance_Updated.routes.voice_routes import voiceBlueprint

app = create_app()
app.register_blueprint(model_blueprint, url_prefix='/model')
app.register_blueprint(voiceBlueprint)


if __name__ == '__main__':
    app.run(host='localhost', port=5030, debug=True, use_reloader=True)