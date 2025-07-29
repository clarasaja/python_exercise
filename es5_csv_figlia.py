from es4_csv_class import CSVFile

class NumericalCSVFile(CSVFile):
    def get_data_as_float(self):
        dati_as_str = super().get_data()  

        dati_as_float = [] #lista di liste

        for elementi in dati_as_str:  # elemento_A: ['data', 'valore', ...,], elemento_B: ['data', 'valore', ...,], ...
            try:
                #copio la data
                nuova_lista_elementi = [elementi[0]]
                for valore in elementi[1:]:  #salta "data"
                    nuova_lista_elementi.append(float(valore))
            except ValueError:
                print(f'Errore di conversione con valore "{valore}" a numerico.')  
                continue
            except Exception as errore:
                print(f'Errore di conversione del valore "{valore}" a numerico: {errore}')  
                break
            dati_as_float.append(nuova_lista_elementi)


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
    
