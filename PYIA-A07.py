import random
def lancar_dados():
    dado_01 = random.randint(1,6)
    print(dado_01)
    dado_02 = random.randint(1,6)
    print(dado_02)
    soma = dado_01 + dado_02
    print(soma)
    return soma
    

lancar_dados()