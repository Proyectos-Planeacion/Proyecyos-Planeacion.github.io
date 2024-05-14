import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\Administrator\Documents\Proyectos_Planeacion\Aplicaciones\Reb_Box_Rose\Bases\Flor_En_Transito.csv")

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost/bases_sunshine')

nombre_tabla = 'flor_en_transito'
df.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)