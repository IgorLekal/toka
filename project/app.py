
from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit, send

mensagem = []

app = Flask(__name__)
io = SocketIO(app)  


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@io.on('MandarMensagemzada')
def send_message_handler(msg):
    emit('pegarMensagem', msg, json=True)


@io.on('Mensagemzada')
def message_handler(msg):
    send(mensagem)


if __name__ == "__main__":
    io.run(app, debug=True)     
