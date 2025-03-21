from flask import Blueprint, request, jsonify
from db import get_db_connection

rewards_bp = Blueprint('rewards', __name__)

@rewards_bp.route('/', methods=['GET'])
def get_rewards():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Rewards')
    rewards = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip([column[0] for column in cursor.description], row)) for row in rewards])

@rewards_bp.route('/', methods=['POST'])
def add_reward():
    conn = get_db_connection()
    cursor = conn.cursor()
    name = request.json['name']
    amount = request.json['amount']
    cursor.execute('INSERT INTO Rewards (name, amount) VALUES (?, ?)', (name, amount))
    conn.commit()
    conn.close()
    return 'Reward added', 201