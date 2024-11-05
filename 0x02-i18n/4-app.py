from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Default locale
DEFAULT_LOCALE = 'en'

@babel.localeselector
def get_locale():
    # Check if the locale is provided in the query parameters
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    return DEFAULT_LOCALE

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run()

