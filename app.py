from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return "Alumno: José Luis Hernandez De La Cruz - Grupo: A"


if __name__ == '__main__' : 
    app.run(debug=True)
