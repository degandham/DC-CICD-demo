import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<h2 style='color:blue'>Welcome to Deloitte Cloud CICD Demo - This is Change#1 </h2>"

def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == '__main__':
    app.run()
