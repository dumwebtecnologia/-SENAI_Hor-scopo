#entada do usuario
print('\n\t\t\t -- Horóscopo --\n')

dia = int(input("Digite o dia de nacimento: "))
mes = int(input("Digite o numero do mes de nacimento: "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        print(f'{mes} Aries')
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        print(f'{mes} Touro')
elif  (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print(f'{mes} Gemios')
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        print(f'{mes} Cancer')
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print(f'{mes} Leão')
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        print(f'{mes} Virgem')
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print(f'{mes} Libra')
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print(f'{mes} Escopião')
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print(f'{mes} Sagitatio')
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        print(f'{mes} Capricornio')
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        print(f'{mes} Aguarios')