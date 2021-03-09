peso = float(input('Qual é o seu peso ? (KG)'))
altura = float(input('Qual é a sua altura ? (M)'))
soma = peso / (altura ** 2)
print('O \033[33mIMC \033[39mdessa pessoa é de {}'.format('%.2f' % soma))
if soma < 18.5:
    print('Seu corpo está ABAIXO do PESO NORMAL!')
elif soma < 25:
    print('Seu corpo está com o PESO NORMAL')
elif soma < 30:
    print('Seu corpo está com SOBREPESO')
elif soma < 40:
    print('Seu corpo está com OBESIDADE!')
elif soma > 40 :
    print('Seu corpo está com OBESIDADE MORBIDA! TOME CUIDADO')