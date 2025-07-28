def sum_mylist(lista):
    if not lista:  # controlla se la lista è vuota
          return None
    somma = 0
    for elemento in lista:
        somma += elemento
    return somma

lista_vuota = []
risultato = sum_mylist(lista_vuota)
print("Somma della lista vuota: {}",risultato)

lista_vuota = []
risultato = sum_mylist(lista_vuota)

print("Somma della lista vuota: {}",risultato)
