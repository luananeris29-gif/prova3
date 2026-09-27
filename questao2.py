altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

if altura < 1.40:
    print("Acesso negado por razões de segurança (altura mínima necessária: 1.40m)")

elif idade < 12:
    print("Acesso autorizado")
    print("Valor do ingresso: R$ 15,00")

elif idade < 60:
    print("Acesso autorizado")
    print("Valor do ingresso: R$ 30,00")

else:
    print("Acesso autorizado")
    print("Valor do ingresso: R$ 15,00")