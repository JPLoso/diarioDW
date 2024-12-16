from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave-secreta' 


usuarios = [{"username": "admin", "password": "1234"}]

anotacoes = {"admin": []}

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    global usuarios  
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
     
        for user in usuarios:
            if user["username"] == username:
                flash("Usuário já existe!")
                return redirect(url_for("cadastro"))
        
        # Adiciona o novo usuário
        usuarios.append({"username": username, "password": password})
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("login"))
    
    return render_template("cadastro.html")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
     
        for user in usuarios:
            if user["username"] == username and user["password"] == password:
                flash("Login bem-sucedido!")
                return redirect(url_for("index"))
        flash("Usuário ou senha incorretos.")
    
    return render_template("login.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/anotacoes/<data>", methods=["GET", "POST"])
def adicionar_anotacao(data):
    data = data.replace("-", "/") 
    if request.method == "POST":
        anotacoes[data] = request.form["anotacao"]
        return redirect(url_for("index"))
    return render_template("anotacoes.html", data=data, anotacao=anotacoes.get(data, ""))


if __name__ == "__main__":
    app.run(debug=True)
