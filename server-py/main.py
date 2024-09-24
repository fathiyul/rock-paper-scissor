from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

choices = {"p1Choice": None, "p2Choice": None}

@socketio.on('join-room')
def on_join(room):
    join_room(room)
    emit('connected')

    room_sockets = socketio.server.manager.rooms.get(f'/{room}', set())
    users = list(room_sockets)

    if len(users) == 3:
        emit('full', "Sorry! Two players are already in this room. Game is on", room=users[2])
        leave_room(room, sid=users[2])
        users.pop()

    emit('updated-users', users, room=room)

    @socketio.on('game-play')
    def on_game_play():
        emit('status', 'Opponent picked! Your turn.', room=room, skip_sid=request.sid)

    @socketio.on('restart')
    def on_restart():
        emit('restart-message', 'Opponent wants to play again', room=room, skip_sid=request.sid)

    @socketio.on('disconnect')
    def on_disconnect():
        emit('disconnected', 'Opponent left the game', room=room, skip_sid=request.sid)

    @socketio.on('p1Choice')
    def on_p1_choice(data):
        choice = data['choice']
        choices['p1Choice'] = choice
        emit('p1Choice', {'choice': choice}, room=room)
        if choices['p2Choice'] is not None:
            declare_winner(room)

    @socketio.on('p2Choice')
    def on_p2_choice(data):
        choice = data['choice']
        choices['p2Choice'] = choice
        emit('p2Choice', {'choice': choice}, room=room)
        if choices['p1Choice'] is not None:
            declare_winner(room)

def declare_winner(room):
    player1 = choices['p1Choice']
    player2 = choices['p2Choice']
    winner = ''

    if player1 == 'scissors':
        if player2 == 'scissors':
            winner = 'draw'
        elif player2 in ['paper', 'lizard']:
            winner = 'player1'
        else:
            winner = 'player2'
    elif player1 == 'paper':
        if player2 == 'paper':
            winner = 'draw'
        elif player2 in ['rock', 'spock']:
            winner = 'player1'
        else:
            winner = 'player2'
    elif player1 == 'rock':
        if player2 == 'rock':
            winner = 'draw'
        elif player2 in ['lizard', 'scissors']:
            winner = 'player1'
        else:
            winner = 'player2'
    elif player1 == 'lizard':
        if player2 == 'lizard':
            winner = 'draw'
        elif player2 in ['spock', 'paper']:
            winner = 'player1'
        else:
            winner = 'player2'
    elif player1 == 'spock':
        if player2 == 'spock':
            winner = 'draw'
        elif player2 in ['scissors', 'rock']:
            winner = 'player1'
        else:
            winner = 'player2'
    else:
        winner = 'draw'

    emit('result', {'winner': winner}, room=room)
    choices['p1Choice'] = None
    choices['p2Choice'] = None

if __name__ == '__main__':
    socketio.run(app, port=4000, debug=True)
