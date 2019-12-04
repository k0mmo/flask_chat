from flask import Flask, render_template
from flask_socketio import SocketIO

ver = "0.0.0"

############## user inputs for server ip and port
print("Flask Chat server Ver " + ver +"\n")
print("Enter Server IP")
print("===============\n")
server_ip = input("> ")
print("\nEnter Port to be used")
print("===============\n")
Port_address = input("> ")

app = Flask(__name__) # app is the name of the object_here
app.config['SECRET_KEY'] = 'passwordgoeshere' # key used by flask to sign cookies, also used by extensions
socketio = SocketIO(app)

@app.route('/') # defines route to a url
def sessions():
    return render_template('session.html') #location jscript code is in located in templates folder

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, host=server_ip, port=Port_address, debug=False)
