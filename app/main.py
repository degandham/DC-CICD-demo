from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:powderblue;'><h1 style='font-family:calibri color:black font-size:300%'>Deloitte Cloud DevOps Demo Website</h1></body>"
    
if __name__ == '__main__':
    app.run()
