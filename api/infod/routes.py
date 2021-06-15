from infod import app, db
from flask import jsonify
from time import perf_counter, sleep

@app.route("/api/v1/latest")
def _get_api_v1_latest():
    t_start = perf_counter()
    doc_count = db.estimated_document_count()
    t_end = perf_counter()
    return jsonify({"status": "ok", "document_count": doc_count, "elapsed": round((t_end - t_start) * 1000, 2)}), 200
