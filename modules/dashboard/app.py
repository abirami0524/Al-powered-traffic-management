from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "Running",
        "traffic_density": random.uniform(0.3, 0.9),
        "accident_alerts": random.choice([True, False]),
        "avg_speed": random.randint(20, 60)
    })

if __name__ == '__main__':
    app.run(debug=True)
