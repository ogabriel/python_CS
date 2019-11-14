# 7. Crie um grd no Bootstrap com flask
class Movie:
    def __init__(self, name, synopsis, img_source):
        self.name = name
        self.synopsis = synopsis
        self.img_source = img_source

from flask import Flask, render_template

app = Flask(__name__)

synopsis = """
A young man is ostracized by his classmates after he bullies a deaf girl to the point where she moves away. Years later, he sets off on a path for redemption. The story revolves around Shôko Nishimiya, a grade school student who has impaired hearing.
"""
img_source = """
https://upload.wikimedia.org/wikipedia/pt/thumb/4/47/Koe-no-Katachi-poster-film.jpg/240px-Koe-no-Katachi-poster-film.jpg
"""
movie = Movie("Koe no Katachi", synopsis, img_source)

@app.route("/movie")
def index():
    return render_template("index.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)

# e no arquivo .html:
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- carrega o bootstrap aqui -->
  </head>

  <body>
    <div class="container">
      <div class="row">
        <img src="{{movie.img_source}}" alt="movie image">
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col">Nome</div>
        <div class="col">
          {{movie.name}}
        </div>
      </div>
      <div class="row">
        <div class="col">Sinopse</div>
        <div class="col">
          {{movie.synopsis}}
        </div>
      </div>
      <button type="button" class="btn btn-primary">Button</button>
    </div>
  </body>
</html>
