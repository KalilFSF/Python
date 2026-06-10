from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/hello') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return '''
Um decorator em Python é uma função que recebe outra função como parâmetro e estende ou modifica seu comportamento sem alterar o código original da função decorada.

Os decorators são amplamente usados para:
- Adicionar funcionalidades extras: Adicionar logs, calcular tempo de execução, verificar permissões ou cachear resultados.
- Reutilizar código: Evitar repetição (princípio DRY - Don't Repeat Yourself) aplicando a mesma lógica a diversas funções.
- Metaprogramação: Alterar o comportamento de funções ou classes de forma limpa e expressiva.

Exemplo de Sintaxe: 
@meu_decorator
def minha_funcao():
    pass

from flask import Flask

app = Flask(__name__)''' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
