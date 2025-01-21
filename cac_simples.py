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
#função de operação

# Exibir opções de operação para o usuário
print("1. ADIÇÃO")
print("2. SUBTRAÇÃO")
print("3. MULTIPLICAÇÃO")
print("4. DIVISÃO")

# Solicitar ao usuário que escolha uma operação
opera = int(input("Escolha uma operação: "))

if opera == 1:
     print("você escolheu ADIÇÃO")
if opera == 2:
     print("você escolheu SUBTRAÇÃO")
if opera == 3:
     print("você escolheu MULTIPLICAÇÃO")
if opera == 4:
     print("você escolheu DVISÃO")
              
# Solicitar ao usuário que insira dois números
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

# Verificar qual operação foi escolhida e chamar a função correspondente
if opera == 1:
     print(f"{num1} somado com {num2} é igual a {add(num1, num2)}")
if opera == 2:
     print(f"{num1} subtraido por {num2} é igual a {sub(num1, num2)}")
if opera == 3:
     print(f"{num1} multiplicado por {num2} é igual a {mult(num1, num2)}")
if opera == 4:
     print(f"{num1} dividido por {num2} é igual a {divi(num1, num2)}")
# Exibir o resultado da operação

# Repetir ou encerrar o programa com base na escolha do usuário