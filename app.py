from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)
@app.route("/")
def inicio():
    return render_template("sitio/index.html")

@app.route("/libros")
def libros():
    return render_template("sitio/book.html")

@app.route("/nosotros")
def nosotros():
    return render_template("sitio/about.html")
@app.route("/administracion")
def AdminStart():
    return render_template("admin/Login.html")
@app.route("/admin/inicio", methods=['POST']  )
def Inicio():
    print(request.form['txtPassword'])
    return render_template("admin/inicio.html")