from infod import app
from flask import jsonify

@app.route("/api/v1/latest")
def _get_api_v1_latest():
    return jsonify({'status': 'ok'}), 200