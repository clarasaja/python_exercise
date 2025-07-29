def sum_mylist(lista):
    if not lista:
        return None

    primo_tipo = type(lista[0])
    
    for elemento in lista:
        if not isinstance(elemento, primo_tipo):
            raise TypeError(f"Tutti gli elementi devono essere dello stesso tipo. Trovato: {type(elemento)}")

    somma = lista[0]
    for elemento in lista[1:]:
        somma += elemento
    return somma

#comunque con la lista mista da errore. Sistemare con try? 

lista_vuota = []
risultato = sum_mylist(lista_vuota)
print("Somma della lista vuota: {}".format(risultato))

lista_numeri = [1,2,3,4]
risultato = sum_mylist(lista_numeri)
print("Somma della lista numeri: {}".format(risultato))

lista_caratteri = ['a','b','c']
risultato = sum_mylist(lista_caratteri)
print("Somma della lista caratteri: {}".format(risultato))

lista_parole = ['prima','seconda','terza']
risultato = sum_mylist(lista_parole)
print("Somma della lista caratteri: {}".format(risultato))

lista_mista = [0,'a','terza']
risultato = sum_mylist(lista_mista)
print("Somma della lista caratteri: {}".format(risultato))