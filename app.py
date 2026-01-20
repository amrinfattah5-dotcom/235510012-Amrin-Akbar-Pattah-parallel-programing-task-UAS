from flask import Flask, jsonify
import dask.dataframe as dd
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join("data", "air_quality.db")

@app.route("/list")
def list_data():
    # Gunakan pandas untuk baca SQLite
    conn = sqlite3.connect(DB_PATH)
    pdf = pd.read_sql("SELECT * FROM classroom_air_quality", conn)
    conn.close()

    # Konversi ke Dask DataFrame untuk "pemrosesan paralel"
    ddf = dd.from_pandas(pdf, npartitions=1)

    # Compute untuk hasil akhir
    df = ddf.compute()
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8123, debug=True)
