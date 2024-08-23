from flask import Flask, render_template, jsonify
from spotify_data import fetch_data #componentes da biblioteca Flask, há também função para renderizar arquivos HTML, e outra para converter python em json

application = Flask(__name__) #caminho correto para localizar os arquivos

@application.route('/')
def index():
    return render_template('index.html') 

@application.route('/data')
def data():
    try:
        data = fetch_data()
        return jsonify(data)
    except Exception as e:
        return str(e), 500  # Retorna o erro como uma resposta com status 500 (Internal Server Error)

if __name__ == '__main__':
    application.run(debug=True, port=5000)
