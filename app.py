from flask import Flask, jsonify, request
from routes.chores import chores_bp
from routes.rewards import rewards_bp
from routes.payments import payments_bp

app = Flask(__name__)

app.register_blueprint(chores_bp, url_prefix='/chores')
app.register_blueprint(rewards_bp, url_prefix='/rewards')
app.register_blueprint(payments_bp, url_prefix='/payments')

@app.route('/')
def home():
    return "Lommepengesystem API"

if __name__ == '__main__':
    app.run(port=5000)