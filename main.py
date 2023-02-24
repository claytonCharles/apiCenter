from flask import Flask , jsonify, request, send_file, Response
from src.Controllers.scraper import *
from flask_cors import CORS
from waitress import serve


app = Flask(__name__)
CORS(app)

@app.route('/scraper/roxin/v1/<string:search>/<int:page>', methods=['GET'])
def scraper(search, page):
    dados = ScraperOlx(search, page)
    return jsonify(dados)

if __name__ == '__main__':
    serve(app)