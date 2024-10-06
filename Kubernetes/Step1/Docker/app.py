from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
import logging
import os
import json
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(level=logging.INFO, format='%(message)s')

# Setup MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client.ping_database
collection = db.pings

# Liveness Probe: Ensure the app is running and can respond to health checks
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/ping', methods=['GET'])
def ping():
    # Record the ping with a timestamp
    result = collection.insert_one({'message': 'ping', 'timestamp': datetime.utcnow()})
    
    # Log the ping
    logging.info(json.dumps({'event': 'PingReceived', 'id': str(result.inserted_id), 'timestamp': datetime.utcnow().isoformat()}))
    
    return jsonify({'message': 'Ping recorded', 'id': str(result.inserted_id)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
