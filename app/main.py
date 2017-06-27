from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:powderblue;'><p><font face='verdana' color='red'>Deloitte Cloud DevOps Demo Website</p></font><p>About us</p></body>"
    
if __name__ == '__main__':
    app.run()
