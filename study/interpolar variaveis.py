 #strings

nome = "João"
idade = 25
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 1234.56
dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s idade> %d" % (nome, idade))
print("Nome {} idade: {}".format(nome, idade))
print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome{1} {1}".format(idade, nome))  
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Nome: {nome} Idade: {idade} {idade} {nome} {idade}".format(nome=nome, idade=idade))
print("nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")


curso = "Python"
print(curso[::-1])