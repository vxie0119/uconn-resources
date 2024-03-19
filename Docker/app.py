'''Main entry point to API'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_class_demo():
    '''Root route'''
    app.logger.debug("Someone called the root route.")
    return '<h1>Hello from Flask & Docker class demo</h1>'

if __name__ == "__main__":
    # app.logger.debug("The flask app is starting up...")
    app.run(debug=True)
