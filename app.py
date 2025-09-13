from flask import Flask, render_template

app = Flask(__name__)

tarefas = [
    {"texto": "Comprar leite", "feito": False},
    {"texto": "Estudar Python", "feito": False},
    {"texto": "Limpar quarto", "feito": False}
]

@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)

from flask import request, redirect, url_for

@app.route("/add", methods=["POST"])
def add():
    tarefa = request.form.get("tarefa")
    if tarefa:
        tarefas.append({"texto":tarefa, "feito": False})
    return redirect(url_for("home"))

@app.route("/remove", methods=["POST"])
def remove():
    tarefa = request.form.get("tarefa")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


