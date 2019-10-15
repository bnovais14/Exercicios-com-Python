n = int(input('Digite um número com 5 digitos:'))
n1=n//10000
print(n1)
n2=n%10000//1000  #o resto decompondo o milhar
print(n2)
n3=n%1000//100
print(n3)
n4=n%100//10
print(n4)
n5=n%10//1
print(n5)


