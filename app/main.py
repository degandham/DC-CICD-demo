from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:red;'><p style='text-align:center'><font face='verdana' color='black' size='6'>Deloitte Cloud Demo Client Web App</p></font><p><script src=‘/home/ec2-user/env.js’></script><script>console.log(env.DEMO_ENV_TYPE)</script></p></body>"
    
if __name__ == '__main__':
    app.run()
