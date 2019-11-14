# 5. Como usamos dados de nossos objetos nas páginas? qual a diretiva?
# R: quando voce for usar um "render_template", para rendenizar a página, voce pode enviar parametros a mais, que estes, por sua vez, vao ser exibidos ou executados na página HTML
# a sintaxe para exibiçao é {{variável ou objeto}} e para comandos {% comando %}

@app.route("/")
def index():
    return render_template("index.html", arg="argumento")

# e no arquivo .html
"""
<body>
  <h1 style="color: blue">Index</h1>
  <p>{{arg}}</p>
</body>
"""


# not part of the answer
# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html", arg="argumento")

# # e no arquivo .html
# """
# <body>
#   <h1 style="color: blue">Index</h1>
#   <p>{{arg}}</p>
# </body>
# """


# @app.route("/string_html")
# def about():
#     return "<h1>Sou uma string!</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

