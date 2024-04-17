from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_url_path='/templates')
requests.packages.urllib3.disable_warnings()

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "ok", "message": "API is healthy"}), 200

@app.route('/', methods=['GET', 'POST'])
def home():
#   return "Hello" 
    return send_from_directory('templates', 'index.html'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
