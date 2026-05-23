from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html', nome = "Kalil", idade = 17)

@app.route("/usuario")
def mostrar_usuario():

    usuario_dados = {"nome": "Ana Souza", "email": "ana.souza@email.com"}

    return render_template('usuario.html', user = usuario_dados)

@app.route("/notas")
def mostrar_notas():
    
    lista_alunos = [
    {"nome": "Bruno Alencar", "notas": [8.0, 7.5, 9.0]},
    {"nome": "Daniela Ribeiro", "notas": [5.5, 6.0, 6.5]},
    {"nome": "Marcos Vinícius", "notas": [9.5, 10.0, 9.0]},
    {"nome": "Patrícia Costa", "notas": [4.0, 7.0, 5.5]}
]
    
    return render_template('notas.html', alunos=lista_alunos)

if __name__ == "__main__":
    app.run(debug=True)