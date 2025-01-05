from flask import Flask, jsonify, render_template
from selenium_script import fetch_trends
from database import save_to_db
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/run-script", methods=["GET"])
def run_script():
    
    proxy_ip = os.getenv("PROXY_IP") # Replace with actual ProxyMesh IP
    try:
        trends, ip_address = fetch_trends(proxy_ip)
        record = save_to_db(trends, ip_address)
        return jsonify(record)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)