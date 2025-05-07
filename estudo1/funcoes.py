def funcao(a,b): 
  print(a+b)
  # aqui temos uma função
  # novamente sem chaves, isso faz perder o estilo da real programação
  # mas tudo bem
  
funcao(2,2) # vamos chama-lá
    # isso deverá imprimir 4
    # as funções lembram uma função anônima ou lambda
    
soma = lambda a, b: a + b
print(soma(2, 2))  # imprime 4