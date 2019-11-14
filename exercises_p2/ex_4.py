# 4. Como funcionam as páginas html no flask? como utilizá-las
# R: De várias formas diferentes, dá pra simplesmente retornar uma string com tags HTMl no "return" do método vinculado a URL, e também da pra usar o método "render_template" pra rendenizar um arquivo externo ".html", que tem de estar numa pasta chamada "templates"
# Ex:
@app.route("/string_html")
def about():
    return "<h1>Sou uma string!</h1>"

@app.route("/arquivo_html")
def index():
    return render_template("index.html")


# not part of the answer
# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route("/arquivo_html")
# def index():
#     return render_template("index.html")


# @app.route("/string_html")
# def about():
#     return "<h1>Sou uma string!</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

