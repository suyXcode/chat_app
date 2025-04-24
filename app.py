from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
import json, os

app = Flask(__name__)
app.secret_key = 'secret!'
socketio = SocketIO(app)

CHAT_HISTORY_FILE = 'chat_data.json'

def load_chat():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_chat(data):
    with open(CHAT_HISTORY_FILE, 'w') as f:
        json.dump(data, f)

chat_history = load_chat()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['room'] = request.form['room']
        return redirect(url_for('chat'))
    return render_template('index.html')

@app.route('/chat')
def chat():
    if 'username' not in session or 'room' not in session:
        return redirect(url_for('index'))
    room = session['room']
    history = chat_history.get(room, [])
    return render_template('chat.html', username=session['username'], room=room, history=history)

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f"{username} has joined the room.", to=room)

@socketio.on('message')
def handle_message(data):
    username = session['username']
    room = session['room']
    msg = f"{username}: {data['msg']}"

    # Save chat
    if room not in chat_history:
        chat_history[room] = []
    chat_history[room].append(msg)
    save_chat(chat_history)

    send(msg, to=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f"{username} has left the room.", to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
