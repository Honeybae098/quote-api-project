# Add 'render_template' to your imports
from flask import Flask, jsonify, render_template
import random
import logging

# ... (the logging config and QUOTES list stay the same) ...
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

QUOTES = [
    {"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."},
    {"author": "Albert Einstein", "quote": "Strive not to be a success, but rather to be of value."},
    {"author": "Mark Twain", "quote": "The secret of getting ahead is getting started."},
    {"author": "Eleanor Roosevelt", "quote": "The future belongs to those who believe in the beauty of their dreams."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Your Name", "quote": "This is my live demo quote for my final presentation!"},
    {"author": "Marie Curie", "quote": "Nothing in life is to be feared, it is only to be understood."}
]


@app.route("/")
def get_quote():
    """Endpoint to get a random quote and display it on a webpage."""
    random_quote = random.choice(QUOTES)
    app.logger.info(f"Serving quote by {random_quote['author']}")
    
    # This line is the main change. It renders the HTML file.
    return render_template(
        'index.html',
        quote_text=random_quote['quote'],
        quote_author=random_quote['author']
    )

@app.route("/health")
def health_check():
    """Health check endpoint for Kubernetes liveness/readiness probes."""
    app.logger.info("Health check successful")
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) 