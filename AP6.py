print('Escolha a atividade:')
escolha = int(input('1.\n2.\n3.\n4.\n'))
match escolha:
  case 1:
    x = input('Digite uma mensagem:\n')
    y = int(input('Digite um número:\n'))
    def mensagem_num():
      print(x)
      print(y)
    if __name__ == '__main__':
      mensagem_num()  
  case 2:
    def calc_idade(x):
      idade = 2025 - x
      return idade
    if __name__ == '__main__':
      x = int(input('Digite o seu ano de nascimento:\n'))
      resultado = calc_idade(x)
      print(f'Sua idade é {resultado}')
  case 3:
    def soma3(x,y,z):
      soma = x + y + z
      return soma
    if __name__ == '__main__':
      x = int(input('Digite o número x'))
      y = int(input('Digite o número y'))
      z = int(input('Digite o número z'))
      resultado = soma3(x, y, z)
      print(f'O resultado é {resultado}')
  case 4:
    #Crie uma função que calcule o imposto sobre o produto, sabendo que produtos que custam menos que R$500 pagam 15% e os que custam mais pagam 25% de imposto
    def calcular_imposto(valor):
      if valor <= 500:
        imposto = valor * 1.15
      else:
        imposto = valor * 1.25
      return imposto 
    if __name__ == '__main__':
      produto = int(input('Digite o valor do produto:\n'))
      resultado = calcular_imposto(produto)
      print(f'O valor do produto com imposto é {resultado}')
