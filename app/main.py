from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<h2 style='color:blue'>Welcome to Deloitte Cloud CICD Demo!</h2>"
    return "<h2 style='color:blue'>This is change#2</h2>"

if __name__ == '__main__':
    app.run()
