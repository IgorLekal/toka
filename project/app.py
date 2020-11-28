
from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
io = SocketIO(app)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') 

@io.on('Mensagemzada')
def send_message_handler(msg):
    emit('pegarMensagem', msg, json=True)

if __name__ == "__main__":
    app.run(debug=True)