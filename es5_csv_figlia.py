from es4_csv_class import CSVFile

class NumericalCSVFile(CSVFile):
    def get_data_as_float(self):
        dati_as_float = super().get_data()  

        for elemento in dati_as_float:  # elemento: ['data', 'valore', ...,]
            for i, valore in enumerate(elemento[1:], start=1):  # parte dall'elemento 2 
                try:
                    elemento[i] = float(valore)  
                except Exception as errore:
                    print(f'Errore di conversione del valore "{valore}" a numerico: {errore}')

        return dati_as_float


###----Utilizzo---####
prova_il_codice = True
if prova_il_codice:
    file_dati_vendite_float = NumericalCSVFile('shampoo_sales.csv') #crea un oggetto CSVFile
    file_dati_vendite_str = CSVFile('shampoo_sales.csv') #crea un oggetto CSVFile


    dati_float = file_dati_vendite_float.get_data_as_float()
    dati_str = file_dati_vendite_str.get_data()

    tipo_float = type(dati_float[1][1]).__name__
    tipo_str = type(dati_str[1][1]).__name__


    print(dati_float[0], "il tipo dei dati dei valori float e' {}".format(tipo_float))
    print(dati_str[0], "il tipo dei dati dei valori str e' {}".format(tipo_str))
    
