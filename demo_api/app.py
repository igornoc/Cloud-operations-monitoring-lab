from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"service": "demo-api", "status": "running"})

@app.get("/health")
def health():
    time.sleep(random.choice([0.05, 0.08, 0.1, 0.2]))
    return jsonify({"status": "healthy"})

@app.get("/slow")
def slow():
    time.sleep(random.choice([1.0, 1.5, 2.0]))
    return jsonify({"status": "slow endpoint simulated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
