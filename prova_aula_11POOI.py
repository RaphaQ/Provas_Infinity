class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")

class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")

class Gato:
    def falar(self):
        print("O gato está miando.")


animal_generico = Animal()
cachorro = Cachorro()
gato = Gato()


animal_generico.falar()
cachorro.falar()
gato.falar()