from flask import Flask, render_template, jsonify
from spotify_data import fetch_data #componentes da biblioteca Flask, há também função para renderizar arquivos HTML, e outra para converter python em json

application = Flask(__name__) #caminho correto para localizar os arquivos

@application.route('/')
def index(): #executa a rota
    return render_template('index.html') 

@application.route('/data')
def data():
    try:
        data = fetch_data() #obter dados dos artistas
        return jsonify(data) #json em http
    except Exception as e: #indica exceções 
        return str(e), 500  #Retorna o erro de status 500 

if __name__ == '__main__':
    application.run(debug=True, port=5000) #indica o servidor

