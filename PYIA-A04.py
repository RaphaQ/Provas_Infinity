# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, 
# em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media (a, b, c):
    valor_media = (a+b+c)/3
    return valor_media


print(media(1,2,3))
