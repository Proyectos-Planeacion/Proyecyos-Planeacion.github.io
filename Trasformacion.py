import mysql.connector, pandas as pd
from flask import Flask, url_for, render_template


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
Productos = " <option value="">" + df["Producto"].unique() + "</option>"

df = df.groupby(['Producto', 'Color', 'Grado'])['Flor Por Ingresar'].sum()
print(df)
df = pd.DataFrame(df)
df_pivoteado = df.pivot_table(index=['Producto', 'Color'], columns='Grado',values='Flor Por Ingresar', aggfunc='sum', fill_value=0)                
tabla_html = df_pivoteado.to_html()
conexion.close()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', df = tabla_html, prod = Productos )



if __name__ == '__main__':
    app.run(debug=True)