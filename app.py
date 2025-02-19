from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to output to stdout
logging.basicConfig(level=logging.INFO)

# Simple global counter
visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    logging.info(f"Visitor from: {request.remote_addr} - Visit count: {visit_count}")
    return f"Hello, world! Your visit has been logged. Total visits: {visit_count}"

if __name__ == '__main__':
    # Use host=0.0.0.0 to ensure the app is accessible externally
    app.run(host='0.0.0.0', port=8000)