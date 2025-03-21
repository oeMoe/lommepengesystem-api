from flask import Blueprint, request, jsonify
from db import get_db_connection

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/', methods=['GET'])
def get_payments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Payments')
    payments = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip([column[0] for column in cursor.description], row)) for row in payments])

@payments_bp.route('/', methods=['POST'])
def add_payment():
    conn = get_db_connection()
    cursor = conn.cursor()
    chore_id = request.json['chore_id']
    amount = request.json['amount']
    cursor.execute('INSERT INTO Payments (chore_id, amount) VALUES (?, ?)', (chore_id, amount))
    conn.commit()
    conn.close()
    return 'Payment added', 201