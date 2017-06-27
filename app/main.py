from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:powderblue;'><h1 style='font-family:calibri'>Deloitte Cloud DevOps Demo Website</h1><p>About us</p></body>"
    
if __name__ == '__main__':
    app.run()
