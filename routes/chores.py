from flask import Blueprint, request, jsonify
from db import get_db_connection

chores_bp = Blueprint('chores', __name__)

@chores_bp.route('/', methods=['GET'])
def get_chores():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Chores')
    chores = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip([column[0] for column in cursor.description], row)) for row in chores])

@chores_bp.route('/', methods=['POST'])
def add_chore():
    conn = get_db_connection()
    cursor = conn.cursor()
    name = request.json['name']
    reward = request.json['reward']
    cursor.execute('INSERT INTO Chores (name, reward) VALUES (?, ?)', (name, reward))
    conn.commit()
    conn.close()
    return 'Chore added', 201