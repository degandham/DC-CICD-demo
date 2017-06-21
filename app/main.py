import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<h2 style='color:blue'>Welcome to Deloitte Cloud CICD Demo - This is Change#1 </h2>

def return_hostname():
    return "<h2 style='color:green'>socket.gethostname()</h2>
    
if __name__ == '__main__':
    app.run()
