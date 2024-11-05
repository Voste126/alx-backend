# 0x02-i18n/2-app.py

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Configuration class for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply the configuration to the Flask app
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)

