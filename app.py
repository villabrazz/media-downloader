"""
Flask backend for the ELTE VAULT demonstration site.

This app serves a single landing page loaded with a 3D WebGL scene,
cinematic animations and a simple AI‑powered recommendation endpoint.

The recommendation system here is a placeholder that randomly picks
from a curated list of models. In a production environment you might
connect this endpoint to a real machine learning model or user profile
service.

To run the application:

    pip install flask
    python app.py

Then open http://127.0.0.1:5000 in your browser.
"""

import random
from flask import Flask, jsonify, render_template


app = Flask(__name__)

# Sample data used by the AI recommendation endpoint.  Each entry
# includes a name, a short description and an image path pointing into
# the ``static/images`` directory.  Replace or extend this list with
# your own content as required.
MODELS = [
    {
        "name": "Aria",
        "description": "Graceful and captivating performer with a magnetic stage presence.",
        "image": "/static/images/aria.jpg",
    },
    {
        "name": "Luna",
        "description": "Energetic artist known for her dynamic performances and charming smile.",
        "image": "/static/images/luna.jpg",
    },
    {
        "name": "Nova",
        "description": "Futuristic star with a daring style and captivating charisma.",
        "image": "/static/images/nova.jpg",
    },
    {
        "name": "Stella",
        "description": "Elegant model celebrated for her sophisticated style and poise.",
        "image": "/static/images/stella.jpg",
    },
    {
        "name": "Raya",
        "description": "Vibrant talent with an electric personality and striking looks.",
        "image": "/static/images/raya.jpg",
    },
]


@app.route("/")
def index() -> str:
    """Render the main landing page."""
    return render_template("index.html")


@app.route("/recommendations")
def recommendations() -> str:
    """Return a list of recommended models in JSON format.

    This endpoint randomly selects three unique models from the
    ``MODELS`` list.  In the future you could replace this logic
    with a call to your own AI model to personalize the results based
    on user behaviour or preferences.
    """
    recommended = random.sample(MODELS, k=3)
    return jsonify(recommended)


if __name__ == "__main__":
    # When running via ``python app.py`` start the Flask development
    # server.  In a production setting you would use a WSGI server
    # such as Gunicorn or uWSGI instead.
    app.run(debug=True, host="0.0.0.0", port=5000)