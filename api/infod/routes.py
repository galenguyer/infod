from infod import app
from flask import jsonify
from time import perf_counter


@app.route("/api/v1/latest")
def _get_api_v1_latest():
    t_start = perf_counter()
    t_end = perf_counter()
    return jsonify({"status": "ok", "elapsed": round((t_end - t_start) * 1000, 2)}), 200
