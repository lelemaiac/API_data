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
        data = datetime.strptime(data, "%d-%m-%Y")
        data_atual = datetime.now()
        data_atual_str = data_atual.strftime("%d/%m/%Y")

        if data_atual == data:
            situacao = "presente"

        elif data_atual > data:
            situacao = "passado"

        else:
            situacao = "futuro"

        diferenca_dias = abs(data_atual - data).days
        diferenca_anos = abs(data_atual.year - data.year)
        diferenca_meses = abs((data_atual.year - data.year)) * 12
        return jsonify({
            "agora": data_atual_str,
            "situacao": situacao,
            "diferenca_dias": str(diferenca_dias),
            "diferenca_meses": str(diferenca_meses),
            "diferenca_anos": str(diferenca_anos)
        })

    except ValueError:
        return jsonify({'error': 'Formato de data incorrecto.'})


if __name__ == '__main__':
    app.run(debug=True)
