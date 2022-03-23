#exercicio 1
def saudacao(msg, nome):
    print(msg, nome)


saudacao('Bem vindo usuario:', 'Michel')

#exercicio 2
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1, 3, 4)

#exercicio 3
def somapercentual(v1, v2):  # v2 é a porcentagem
    v3 = v1 * (v2 / 100)
    soma = v1 + v3
    return soma

somadopercentual = (somapercentual(2, 10))
print(somadopercentual)

def fizzbuzz(n1):
    if n1 % 2 == 0 and n1 % 5 == 0:
        return 'fizzbuzz'
    elif n1 % 2 == 0:
        return 'fizz'
    elif n1 % 5 ==0:
        return 'buzz'
    else:
        return n1


fizz= fizzbuzz(20)
print(fizz)