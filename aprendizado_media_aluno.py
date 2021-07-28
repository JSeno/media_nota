#Aprendizado Média de Aluno
nota1 = float(input('Coloque a nota da primeira prova: '))
nota2 = float(input('Coloque a nota da segunda prova: '))
media = (nota1 + nota2)/2

if media >=7:
    print('Parabéns você está: Aprovado')
else:
    print('É uma pena mas você está: Reprovado')
