import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:red;'><p style='text-align:center'><font face='verdana' color='black' size='6'>Deloitte Cloud Demo Client Web App os.environ["DEMO_ENV_TYPE"]</p></font></body>"
    
if __name__ == '__main__':
    app.run()
