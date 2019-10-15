print ('Calcule o volume de uma lata de óleo, em que pi é igual a 3.14, o raio é 4cm e  a altura é de 10cm')
pi = float(input('Digite o valor de pi:'))
r = int(input('Digite o valor do raio:'))
h = int(input('Digite o valor da altura:'))
res = pi*r**2*h
print ('o volume dessa lata de óleo é igual a', format (res, '.2f'))

