from flask import Flask, render_template, jsonify
from spotify_data import fetch_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/data')
def data():
    try:
        data = fetch_data()
        return jsonify(data)
    except Exception as e:
        return str(e), 500  # Retorna o erro como uma resposta com status 500 (Internal Server Error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
