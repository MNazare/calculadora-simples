# Definir funções para cada operação (adição, subtração, multiplicação, divisão)



# Função para adição
def add(num1, num2):
       return num1 + num2

# Função para subtração
def sub(num1, num2):
       return num1 - num2

# Função para multiplicação
def mult(num1, num2):
   return num1 * num2

# Função para divisão
def divi(num1, num2):
       if num2 == 0:
             return("nada de divisão por zero")
       else:
             return num1/num2

# Exibir opções de operação para o usuário
print("1. ADIÇÃO")
print("2. SUBTRAÇÃO")
print("3. MULTIPLICAÇÃO")
print("4. DIVISÃO")

# Solicitar ao usuário que escolha uma operação
while True:
        opera = int(input("Escolha o tipo de operação 1/2/3/4: "))
         if opera != 1,2,3,4:
              print("você deve escolher um numero válido")
              break
         else:
              
# Solicitar ao usuário que insira dois números
num1 = float(input("digite o primeiro numero"))
num2 = float(input("digite o segundo numero"))

# Verificar qual operação foi escolhida e chamar a função correspondente
if opera == 1
# Exibir o resultado da operação

# Repetir ou encerrar o programa com base na escolha do usuário