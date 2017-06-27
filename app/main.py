import os
from flask import Flask

app.config.from_object(os.environ['DEMO_ENV_TYPE'])
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:red;'><p style='text-align:center'><font face='verdana' color='black' size='6'>Deloitte Cloud Demo Client Web App</p></font></body>"

if __name__ == '__main__':
    app.run()
