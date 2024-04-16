from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "ok", "message": "API is healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
