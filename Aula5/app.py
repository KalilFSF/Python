from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/projetos')
def projetos():    
    return render_template('projetos.html')

@app.route('/hobbies')
def hobbies():    
    return render_template('hobbies.html')



if __name__ == '__main__':
    app.run(debug=True)
