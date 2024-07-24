from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "This is working!"}

@app.route('/test')
def test_route():
    return {"message": "Test route"}
