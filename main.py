from flask import Flask, make_response, jsonify, request
from db import Produtos
app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def getProdutos():
    return make_response(
        jsonify(
            mensagem = 'Listagem de Produtos',
            produto = Produtos
        )
    ) 
    
@app.route('/produtos', methods=['POST'])
def postProdutos():
    produto = request.json
    Produtos.append(produto)
    return getProdutos()

app.run()


