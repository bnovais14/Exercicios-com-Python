import math
custo = float (input ("Custo do espetáculo:"))
convite = float (input("Valor do convite:"))
qtde = custo/convite
qtde23 = custo*1.23/convite
print ("Qtde para ter lucro: %d" %math.ceil(qtde))
print ("Qtde para ter lucro 23%%: %d " %math.ceil(qtde23))
