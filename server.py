from flask import Flask, render_template, current_app as app
from flask_cors import CORS

app = Flask(__name__)

 
CORS(app)

@app.route("/")
def index():
    name=''
    print(name)
    return render_template('test.html',name=name)

@app.route("/name", methods=['GET'])
def send_name():
    return render_template()
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')