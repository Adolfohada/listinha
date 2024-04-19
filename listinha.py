'''
Exercicio da listinha
1:
while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            break
        else:
            print("O numero deve ser entre 0 e 10")
    else:
        print("Você deve digitar um numero! ")

2:
a)
while True:
    nome = input("Diga seu nome: ")
    if len(nome)>=3:
        break
b)
while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        idade = int(nota)
        if nota >= 0 and nota <= 150:
            break
        else:
            print("O numero deve ser entre 0 e 150")
    else:
        print("Você deve digitar um numero! ")
c)
salario = input("Diga seu salario: ")
while not salario.isnumeric():
    salario = input("Diga seu salario: ")

d)
sx = input("Diga f ou m\n ->")
while sx != 'f' and sx != 'm':
    sx = input("Diga f ou m \n->")
e)
ec = input("Diga s,c,v,d:\n->")
while not (ec== 's' or ec == 'c' or ec == 'v' or ec =='d'):
    print("Opção inválida ")
    ec = input("Diga s,c,v,d,:\n->")
3)
a = 80
b = 200
anos = 0
while a < b:
    a*=1.03
    b*=1.015
    anos +=1
print(anos)

4)
qtd = 0
soma = 0
while qtd < 5:
    num = input(f"Diga o {qtd+1} numero: ")
    while not num.isnumeric():
        print("Deve ser numero ")
        num = input(f"Diga o {qtd+1} numero: ")
    num = int(num)
    soma +=num
    qtd += 1
print(f"A soma dos numeros foi  {soma} e a media foi {soma/qtd}")


5)
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if a > b:
    aux = a
    a=b
    b = aux
while a<=b:
    print(a)
    a+=1

6)
while True:
    usuario = input("Diga seu nome de usuario: ")
    senha = input("Diga sua senha: ")
    if senha != usuario:
        break
        print("Nome de usuario não pode ser igual a senha ")
7)
num = 1
while num <=10:
    print(f"Tabuada do { num}")
    i = 1
    while i <= 10:
        print(f"{num}* {i} = {num*i}")
        i+= 1
    num+= 1
    print()

8)
a =1
b =1
i = 0
while i  < 10:
    c = a + b
    print(f"{c}, ")
    a=b
    b=c
    i+=1

9)
qtd = 0
pares = 0
while qtd <10:
    num = input(f"Diga o {qtd+1} numero: ")
    while not num.isnumeric():
        num = input(f"diga o {qtd+1} numero: ")
    num = int(num)
    if num % 2== 0:
        pares +=1
    qtd +=1
print(f"Vc digitou {pares} pares e {qtd - pares} impares")

10)
num = 5
fatorial = num
fatorial_string = f"{num}! = {num}"
while num>1:
    num -= 1
    fatorial *= num
    fatorial_string += f"*{num}"
    print(fatorial_string)
fatorial_string += f" = {fatorial}"
print(fatorial_string)

11)
num = 71
i = 2
while i < num**0.5:
    print(f"{num} % {i} = {num%i}")
    if num % i == 0:
        print("Não é primo! ")
        break
    i+=1
if i >= num**0.5:
    print("é primo")

12)
igual o exercicio 4

13)
salario = 1000
taxa = 0.015
partida = 1995
while partida < 2000:
    salario *=1 + taxa
    taxa *= 2
    partida += 1
print(salario)



'''














