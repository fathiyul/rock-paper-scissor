# Getting started with the server, python version

This is a Python version of the server. It uses Flask and Flask-SocketIO to handle real-time communication between players.

## Installation

Install the required packages:

```
pip install flask flask-socketio flask-cors
```

## Usage

To start the server, run the following command in your terminal:

```
python main.py
```

The server will start running on `http://localhost:4000`.

## API

The server uses WebSocket events for communication. Here are the main events:

- `join-room`: Join a game room
- `game-play`: Notify when a player has made a choice
- `restart`: Request to restart the game
- `p1Choice`: Player 1's choice
- `p2Choice`: Player 2's choice

The server emits the following events:

- `connected`: Confirms successful connection
- `updated-users`: Provides updated list of users in a room
- `full`: Notifies when a room is full
- `status`: Provides game status updates
- `restart-message`: Notifies about restart requests
- `disconnected`: Notifies when an opponent disconnects
- `result`: Provides the game result
