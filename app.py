from flask import Flask, render_template, request

app = Flask(__name__)

listaCliente = []
listaCelular = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/guardar", methods=["POST"])
def guardar():
    nCliente = request.form["cliente"]
    nCelular = request.form["celular"]
    listaCliente.append(nCliente)
    listaCelular.append(nCelular)
    return render_template('index.html', listaM=listaCelular, listaP=listaCliente)


@app.route("/buscar", methods=["POST"])
def buscar():
    nCliente = request.form["bCliente"]

    if (nCliente in listaCliente):
        pos = listaCliente.index(nCliente)

        return render_template("index.html", vCli=listaCliente[pos], vCel=listaCelular[pos])
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(port=700000, debug=True)