from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return("hello")


def about():
    return "hello"

if __name__ == '__main__':
    app.run()