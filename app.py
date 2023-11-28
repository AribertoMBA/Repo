from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Nada de Hello World, hoje é dia das bruxas"