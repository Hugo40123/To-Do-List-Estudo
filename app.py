from flask import Flask, render_template

app = Flask(__name__)

tarefas = ["Comprar leite", "Estudar Python", "Limpar quarto"]

@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)

from flask import request, redirect, url_for

@app.route("/add", methods=["POST"])
def add():
    tarefa = request.form.get("tarefa")
    if tarefa:
        tarefas.append(tarefa)
    return redirect(url_for("home"))

@app.route("/remove", methods=["POST"])
def remove():
    tarefa = request.form.get("tarefa")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

##Notebook
##01

