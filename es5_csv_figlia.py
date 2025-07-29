from es4_csv_class import CSVFile

class NumericalCSVFile(CSVFile):
    def get_data_as_float(self):
        dati_as_float = super().get_data()
        #vorrei farla in-place
        for i, elementi in enumerate(dati_as_float):
            if i != 0:
                try:
                    for j,e in enumerate(elementi):
                        dati_as_float[i][j] = float(e)
                    #print(elementi)

                except Exception as errore:
                    print('Errore di conversione del valore "{}" a numerico: "{}"'.format(elementi, errore))
                    break


        return dati_as_float
    

###----Utilizzo---####
prova_il_codice = True
if prova_il_codice:
    file_dati_vendite_float = NumericalCSVFile('shampoo_sales.csv') #crea un oggetto CSVFile
    file_dati_vendite_str = CSVFile('shampoo_sales.csv') #crea un oggetto CSVFile


    dati_float = file_dati_vendite_float.get_data()
    dati_str = file_dati_vendite_str.get_data()

    tipo_float = type(dati_float[1][1]).__name__
    tipo_str = type(dati_str[1][1]).__name__

    print(dati_float[1][1])
    print(type(dati_float[1][1]))
    print(float(dati_float[1][1]))
    print(type(float(dati_float[1][1])))

    print(dati_float[0], "il tipo dei dati dei valori float e' {}".format(tipo_float))
    print(dati_str[0], "il tipo dei dati dei valori str e' {}".format(tipo_str))
    
