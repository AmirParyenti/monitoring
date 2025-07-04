from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a counter metric
REQUEST_COUNT = Counter('web_requests_total', 'Total number of HTTP requests')

@app.route('/')
def index():
    REQUEST_COUNT.inc()  # Increment the counter
    return "Hello, world!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
