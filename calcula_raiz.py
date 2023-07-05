def calcula_raiz (numero):
    for i in range (numero):
        if i * i == numero:
            return f'A raíz do número {numero} é igual a {i}'
            break
        if i * i > numero:
            return 'Este número não tem raíz exata!'
            break
