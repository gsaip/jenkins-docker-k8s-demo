from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.getenv('APP_ENV', 'Development')
    return jsonify({"message": f"Hello from DevOps Pipeline! Running in {env}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
