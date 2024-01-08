from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)

@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello, cross-origin-world!"

@app.after_request
def add_headers(response):
    # Add headers here
    response.headers['Custom-Header'] = 'Some custom value'
    response.headers['Another-Header'] = 'Another value'
    return response

if __name__ == '__main__':
    app.run(debug=True)
