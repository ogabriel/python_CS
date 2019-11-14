# 6. Como podemos usar o ​ for ​ em uma página html no ​ flask​ ? Por que isso acontece?
# R: da para usar o for com a sintaxe de comandos do jinja que é {% comando %}, nesse caso é possivel usar o comando for para tal, a única diferença do uso do "for" num arquivo .py normal, é que para finaliza-lo tem de usar o comando "endfor"

@app.route("/")
def index():
    return render_template("index.html", args=["foo", "bar"])

# e no arquivo .html
"""
<body>
    {% for a in args %}
        <p>{{a}}</p>
    {% endfor %}
</body>
"""


# this code will not be used
# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html", args=["foo", "bar"])

# # e no arquivo .html
# """
# <body>
#     {% for a in args %}
#         <p>{{a}}</p>
#     {% endfor %}
# </body>
# """

# if __name__ == "__main__":
#     app.run(debug=True)

