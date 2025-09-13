from flask import Flask, render_template

app = Flask(__name__)

tarefas = [
    {"texto": "Comprar leite", "feito": False, "prazo": None},
    {"texto": "Estudar Python", "feito": False, "prazo": None},
    {"texto": "Limpar quarto", "feito": False, "prazo": None}
]

@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)

from flask import request, redirect, url_for
from datetime import datetime

@app.route("/add", methods=["POST"])
def add():
    tarefa = request.form.get("tarefa")
    prazo_str = request.form.get("dataHora")
    prazo_formatado = None
    categoria = request.form.get("categoria")

    if prazo_str:
        prazo = datetime.fromisoformat(prazo_str)
        prazo_formatado = prazo.strftime("%d/%m/%Y %H:%M")
    if tarefa:
        tarefas.append({"texto":tarefa, "feito": False, "prazo": prazo_formatado, "categoria": categoria})
    return redirect(url_for("home"))

@app.route("/concluir", methods=["POST"])
def concluir():
    tarefa_texto = request.form.get("tarefa")
    for tarefa in tarefas:
        if tarefa["texto"] == tarefa_texto:
            tarefa["feito"] = True
            break
    return redirect(url_for("home"))

@app.route("/remove", methods=["POST"])
def remove():
    tarefa_texto = request.form.get("tarefa")
    for tarefa in tarefas:
        if tarefa["texto"] == tarefa_texto:
            tarefas.remove(tarefa)
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


