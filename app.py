from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime

app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                         title='Flask API - SENAI',
                         version='1.0')
spec.register(app)

@app.route('/verificar-data/<data>')
def verificar_data(data):
    """
    API para calcular a diferença entre duas datas.

    ## Endpoint:
     /verificar-data/<data>

    ## Parâmetros:
    "data" **Data no formato "DD-MM-YYYY"** (exemplo: 20-03-2025)

    ## Respostas (JSON):
    ```json

    {
    "diferenca_dias":
    "diferenca_meses":
    "diferenca_anos":
    "situacao":
        }

    ## Erros possíveis (JSON):
     Se data não estiver no formato "DD-MM-YYYY", rertorna erro ***400
     Bad Request***:
         ```json
    """

    try:
        data= datetime.strptime(data, "%d-%m-%Y")
        data_atual = datetime.now()
        __repr_data__ = data_atual.strftime("%d/%m/%Y")

        if data_atual == data:
            situacao = "presente"

        elif data_atual > data:
            situacao = "passado"

        else:
            situacao = "futuro"

        diferenca_dias = data_atual.day - data.day
        diferenca_mes = data_atual.month - data.month
        diferenca_ano = data_atual.year - data.year
        return jsonify({"agora": __repr_data__, "situacao": situacao, "diferenca_dias": diferenca_dias,
                        "diferenca_meses": diferenca_mes, "diferenca_anos": diferenca_ano})

    except ValueError:
        return jsonify({'error': 'Formato de data incorrecto.'})

if __name__ == '__main__':
    app.run(debug=True)