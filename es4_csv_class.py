
class CSVFile():
    def __init__(self,nomefile):
        self.nomefile = nomefile

        # Provo ad aprirlo e leggere una riga [ho guardato la soluzione :3]
        self.can_read = True
        try:
            file_da_aprire = open(self.nomefile, 'r')
            file_da_aprire.readline()
        except Exception as errore:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(errore))


    def __str__(self):
        return "Questo è un file CSV: {}".format(self.nomefile)
    
    def __repr__(self):
        return f"CSVFile('{self.nomefile}')"
    
    def get_data(self):
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None
        else:
            dati = []
            with open(self.nomefile,'r') as miofile:
                for riga in miofile:
                    elementi = riga.split(',')
                    
                    if elementi[0] != 'Date':
                        data = elementi[0]
                        valore = float(elementi[1])
                        dati.append([data,valore])
            return dati
        


###----Utilizzo---####
file_dati_vendite = CSVFile('shampoo_sales.csv') #crea un oggetto CSVFile
file_errato = CSVFile('shampoo_sales.cs') #fa il print dell'excetpion

dati = file_dati_vendite.get_data()
dati2 = file_errato.get_data()


print(dati)
print(dati2)
