import mysql.connector, pandas as pd
from flask import Flask, url_for, render_template, \
    request


conexion = mysql.connector.connect(
user="root",
password="",  # Asegúrate de que aquí va tu contraseña real, si la hay
host="localhost",
database="bases_Sunshine",
port="3306"
)   



df = pd.read_sql('SELECT * FROM flor_en_transito', con=conexion)
# df = df[df["Producto"] == "ROSE"]     
df = df[df["Flor Por Ingresar"] != 0]
Productos = " <option value="  + df["Producto"].unique() + ">" + df["Producto"].unique() + "</option>"

df = df.groupby(['Producto', 'Color', 'Grado'])['Flor Por Ingresar'].sum()
print(df)
df = pd.DataFrame(df)
df_pivoteado = df.pivot_table(index=['Producto', 'Color'], columns='Grado',values='Flor Por Ingresar', aggfunc='sum', fill_value=0)                
tabla_html = df_pivoteado.to_html()
conexion.close()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html' )

@app.route("/tabla")
def tabla():
    return render_template('tabla.html', df = tabla_html, prod = Productos )

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/get_product", methods=['GET', 'POST'])
def get_product():
    select = request.form.get('producto')

    conexion = mysql.connector.connect(
    user="root",
    password="",  # Asegúrate de que aquí va tu contraseña real, si la hay
    host="localhost",
    database="bases_Sunshine",
    port="3306"
)   
    df = pd.read_sql('SELECT * FROM flor_en_transito', con=conexion)
    Productos = " <option value="  + df["Producto"].unique() + ">" + df["Producto"].unique() + "</option>"
    df = df[df["Producto"] == select]     
    df = df[df["Flor Por Ingresar"] != 0]

    df = df.groupby(['Producto', 'Color', 'Grado'])['Flor Por Ingresar'].sum()
    print(df)
    df = pd.DataFrame(df)
    df_pivoteado = df.pivot_table(index=['Producto', 'Color'], columns='Grado',values='Flor Por Ingresar', aggfunc='sum', fill_value=0)                
    tabla_html = df_pivoteado.to_html()
    conexion.close()
    return render_template('tabla.html', df = tabla_html, prod = Productos, select = select )



if __name__ == '__main__':
    app.run(debug=True)