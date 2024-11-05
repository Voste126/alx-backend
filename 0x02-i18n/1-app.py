# 0x02-i18n/1-app.py

from flask import Flask, render_template
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

@app.route('/')
def index():
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=Tru

