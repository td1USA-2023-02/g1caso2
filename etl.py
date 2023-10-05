import pandas as pd
pd.set_option('display.max_columns', None)

archivo_origen = "g1caso2/Super Store.xlsx"

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_excel(archivo_origen)
print(datos.head())


residuos_variables = ["Row ID","Customer ID","Customer Name","Country","Postal Code","Product ID",]

data_limpiada=datos.drop(residuos_variables, axis=1)

data_limpiada.to_csv('datos_limpiados.csv', index=False)


data2 = "g1caso2\datos_limpiados.csv"

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datal = pd.read_csv(data2)
print(datal.head())



datal["Ship Date"] = pd.to_datetime(datal["Ship Date"],format='%Y-%m-%d')
datal["Order Date"] = pd.to_datetime(datal["Order Date"],format='%Y-%m-%d')  

datal ["dias_demora"] = (datal["Ship Date"]-datal["Order Date"]).dt.days
print(datal.head())

datal = datal.sort_values(by="dias_demora",ascending=False)

print(datal.head())

def perdida (Profit):
    if Profit > 0:
        return 0
    else:
        return 1
    
datal["perdida "] = datal["Profit"].apply( perdida )

print(datal.head())


datal.to_csv('dta_flimpiadav2.csv', index=False)



