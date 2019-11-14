# 1. Crie uma classe livro em python que possua os atributos nome, autor, sinopse e  editora, seus dados precisam ser privados e populados no método construtor.

class Book:
    def __init__(self, name, author, sinopsis, publisher):
        self.__name = name
        self.__author = author
        self.__sinopsis = sinopsis
        self.__publisher = publisher

