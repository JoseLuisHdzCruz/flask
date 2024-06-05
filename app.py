from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return "José Luis Hernandez De La Cruz - 20211032"


if __name__ == '__main__' : 
    app.run(debug=True)
