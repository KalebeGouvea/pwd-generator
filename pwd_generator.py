import random as rd
class pwdGen:
    E = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$*¨%!&@#$*¨%!&@#$*¨%!&'
    C = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    c = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def size():
        while True:
            try:
                sz = int(input('Digite o tamanho para a senha: '))
                break
            except:
                print('Tamanho inválido. Digite um número inteiro para o tamanho da senha.')
        return sz
    
    def chars():
        chars = str(input('Deve conter caracteres especiais (s/n): '))
        while chars != 's' and chars != 'n':
            print('Resposta invalida. Responda apenas s ou n.')
            chars = str(input('Deve conter caracteres especiais (s/n): '))
        if chars == 's':
            chars = pwdGen.E
        else:
            chars = pwdGen.C
        return chars

    def gerar(a, b):
        while True:
            output = rd.choices(a, k = b)
            new_pwd = ''.join(output)
            print(new_pwd)
            print()
            q = input('Deseja gerar uma nova senha (s/n)? ')
            while q != 's' and q != 'n':
                print('Resposta invalida. Responda apenas s ou n.')
                q = input('Deseja gerar uma nova senha (s/n)? ')
            if q == 's':
                continue
            else:
                break

print('#######GERADOR DE SENHAS#######')
print('Descrição: Esse programa gera senhas aleatórias baseadas no tamanho e tipo de caracteres informados')       
print()
sz = pwdGen.size()
chars = pwdGen.chars()

print('A senha gerada é: ')
pwdGen.gerar(chars, sz)