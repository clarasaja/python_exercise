def open_csv(csv_file):
    dati = []
    with open (csv_file,'r') as mio_file:
        for riga in mio_file:
            elementi = riga.split(',')
        
        if elementi[0] != 'Date':
            data = elementi[0]
            valore = float(elementi[1])
        dati.append([data,valore])
    return dati


def sum_csv(lista):
    if not lista:
        return None

    primo_tipo = type(lista[0])
    
    somma = lista[0]
    for elemento in lista[1:]:
        somma += elemento
    return somma


dati = open_csv('shampoo_sales.csv') #lista di liste dati.append([data,valore])
valori = [valore for data,valore in dati]

somma = sum(valori)
print('La somma è {}'.format(somma))