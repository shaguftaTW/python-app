from flask import Flask, jsonify
import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.date.today().strftime("%Y-%m-%d"),
        'hostname': socket.gethostname(),
        'message': 'Hello World'    
        })


@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'UP'    
        }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")



#'/api/v1/details'
#'/api/v1/healthz'