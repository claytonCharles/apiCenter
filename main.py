from flask import Flask , jsonify, request, send_file, Response
from src.Controllers.scraper import *
from flask_cors import CORS, cross_origin
import pandas as pd
import io
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route('/scraper/roxin/v1/<string:search>/<int:page>', methods=['GET'])
def scraper(search, page):
    dados = ScraperOlx(search, page)
    return jsonify(dados)

@app.route('/xlsx/roxin/v1/', methods=['POST'])
def xlsx():
    by = TableXlsx(request.get_json())

    return send_file(by, mimetype='application/vnd.ms-excel',download_name="PlhanilhaScrape.xlsx", as_attachment=True)

if __name__ == '__main__':
    serve(app, port=5000, host='localhost')