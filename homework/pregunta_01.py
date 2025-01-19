# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Funcion que carga los datos
def load_data():
    df = pd.read_csv('files/input/shipping-data.csv')
    return df

# Funcion que crea la grafica para los envios por bodega(A-F)
def shipping_per_warehouse(df):
    df = df.copy()
    # Se crea una figura limpia
    plt.figure

    # Se toman los datos necesarios para graficar
    # Cantidad de envios por bodega
    counts = df.Warehouse_block.value_counts()

    # Transformamos los datos en una grafica de barras
    counts.plot.bar(
        title = 'Shipping per Warehouse',
        xlabel = 'Warehouse block',
        ylabel = ' Record count',
        color = 'tab:blue',
        fontsize = 8,
    )

    # Se pone mas bonita
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/shipping_per_warehouse.png')
    

# Funcion que crea la grafica que muestra la forma de hacer los envios
def mode_of_shipment(df):
    df = df.copy()
    # Se crea una figura limpia
    plt.figure()

    # Se toman los datos necesarios para graficar
    # Cantidad de envios medidos por su medio de transporte
    counts = df.Mode_of_Shipment.value_counts()

    # Se transforman los datos a un grafico de torta(pie)
    counts.plot.pie(
        title = 'Mode of shipment',
        wedgeprops = dict(width=0.35),
        ylabel = '',
        colors = ['tab:blue', 'tab:orange', 'tab:green'],
    )

    # Se guarda la figura
    plt.savefig('docs/mode_of_shipment.png')


# Función que crea la grafica del promedio de la calificación de los usuarios
def average_customer_rating(df):
    df = df.copy()
    # Se crea una figura limpia
    plt.figure()

    # Se toman los datos necesarios para grafica
    # Calificación media de los clientes
    df = (df[['Mode_of_Shipment', 'Customer_rating']].groupby('Mode_of_Shipment').describe())
    df.columns = df.columns.droplevel()
    df = df[['mean', 'min', 'max']]

    # Se hace un grafico de barras horizontal
    plt.barh(
        y = df.index.values,
        width = df['max'].values - 1,
        left = df['min'].values,
        height = 0.9,
        color = 'lightgray',
        alpha = 0.8,
    )

    # Verde positivo, naranja malo
    colors = ['tab:green' if value >= 3.0 else 'tab:orange' for value in df['mean'].values]
    plt.barh(
        y = df.index.values,
        width = df['mean'].values - 1,
        left = df['min'].values,
        color = colors,
        height = 0.5,
        alpha = 1.0,
    )

    # Estetica y mejor entendimiento en la imagen
    plt.title('Average Customer Rating')
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    
    # Se guarda la figura
    plt.savefig('docs/average_customer_rating.png')



# Función que crea la grafica de la distribución del peso
def weight_distribution(df):
    df = df.copy()
    # Se crea una figura limpia
    plt.figure()

    # Se crea un histograma de los datos
    df.Weight_in_gms.plot.hist(
        title = ' Shipped Weight Distribution',
        color = 'tab:orange',
        edgecolor = 'white',
    )

    # Estetica y mejor entendimiento en la imagen
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Se guarda la imagen
    plt.savefig('docs/weight_distribution.png')


# Función que inicia el programa
def pregunta_01():
    # Se crea la ruta en donde se guardan los archivos
    ruta = 'docs'
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    
    # Se cargan los datos
    df = load_data()

    # Se crea la figura shipping_per_warehouse.png
    shipping_per_warehouse(df)

    # Se crea la figura mode_of_shipment.png'
    mode_of_shipment(df)

    # Se crea la figura average_customer_rating.png
    average_customer_rating(df)

    # Se crea la figura weight_distribution.png
    weight_distribution(df)

    # Se crea un archivo hmtl que sirva como dashboard
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Shippping dashboard example</h1>
            <div style="width:45%:float:left">
                <img src="shipping_per_warehouse.png" alt="Fig 1">
                <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%:float:left">
                <img src="average_customer_rating.png" alt="Fig 3">
                <img src="weight_distribution.png" alt="Fig 1">
            </div>  
        </body>
    </html>
    """
    # Crear y guardar el archivo HTML
    with open('docs/index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
pregunta_01()