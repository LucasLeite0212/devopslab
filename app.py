from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Leite"

if __name__ == '__main__':
    app.run()