from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:powderblue;'><p><font face='verdana' color='red' size='8'>Deloitte Cloud Demo Customer Application</p></font></body>"
    
if __name__ == '__main__':
    app.run()
