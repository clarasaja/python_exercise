
class CSVFile():
    def __init__(self,nomefile):
        self.nomefile = nomefile

    def __str__(self):
        return "Questo è un file CSV: {}".format(self.nomefile)
    
    def __repr__(self):
        return f"CSVFile('{self.nomefile}')"
    
    def get_data(self):
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

dati = file_dati_vendite.get_data()

print(dati)
