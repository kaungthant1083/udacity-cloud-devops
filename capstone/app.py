from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h2 style='text-align: center;'>Welcome to Udacity Capstone Project!</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) 