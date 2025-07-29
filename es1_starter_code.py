def mia_funzione(argomento1,argomento2):
    print("Funzione: Numero {} dell'elemento {}".format(argomento1,argomento2))


print("Hello world!")

x = 25
print('Ho {} anni'.format(x))
print('BUGIA')

for i in range(10): #numeri da 0 a 9 
    print(i)

my_list = range(1,21) #creo una lista con i numeri da 1 a 20
for numero in  my_list:
    print("Elemento {}".format(numero))

for (i,numero) in  enumerate(my_list):
    print("Numero {} dell'elemento {}".format(i,numero))
    mia_funzione(i,numero)
