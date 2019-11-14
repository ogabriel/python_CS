# 3. Para que serve @app.route no flask? como utilizá-la?
# R: É um decorator que serve para vincular uma URL a uma funçao que precede a declaraçao de rota

@app.route("/ex3")
def exercise_3():
    return "Exercício 3"

# o código acima vincula a URL host/ex3 a o método "exercise_3"

# from flask import Flask
# app = Flask(__name__)

# @app.route("/ex3")
# def exercise_3():
#     return "Exercício 3"

# if __name__ == "__main__":
#     app.run(debug=True)

