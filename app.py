from flask import Flask, jsonify
import random
import logging

# Configure logging to show info-level messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# A simple list of quotes stored in memory
QUOTES = [
    {"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."},
    {"author": "Albert Einstein", "quote": "Strive not to be a success, but rather to be of value."},
    {"author": "Mark Twain", "quote": "The secret of getting ahead is getting started."},
    {"author": "Eleanor Roosevelt", "quote": "The future belongs to those who believe in the beauty of their dreams."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Your Name", "quote": "This is my live demo quote for my final presentation!"},
    # ... other quotes
]


@app.route("/")
def get_quote():
    """Endpoint to get a random quote."""
    random_quote = random.choice(QUOTES)
    app.logger.info(f"Serving quote by {random_quote['author']}")
    return jsonify(random_quote)

@app.route("/health")
def health_check():
    """Health check endpoint for Kubernetes liveness/readiness probes."""
    app.logger.info("Health check successful")
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Run the app, listening on all network interfaces on port 8080
    app.run(host='0.0.0.0', port=8080)