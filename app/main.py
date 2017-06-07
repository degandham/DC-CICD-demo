from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return 'Welcome to Deloitte Cloud CICD Demo!'

if __name__ == '__main__':
    app.run()
