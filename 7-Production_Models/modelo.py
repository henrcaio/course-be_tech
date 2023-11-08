# Importando Bibliotecas
import pandas as pd
from sklearn.cluster import KMeans
import joblib
import warnings

warnings.filterwarnings("ignore")

# Importando CSV
df_fakebills = pd.read_csv("fake_bills_unsuperv.csv", index_col=0)
df_fakebills.head()

# Dropando nulos
df_fakebills.dropna(inplace=True)

# Treinando modelo
kmeans_md = KMeans(n_clusters=2, random_state=42)
kmeans_md.fit(df_fakebills)

# Salvar o modelo em formado pkl usando joblib
joblib.dump(kmeans_md, "modelo_treinado.pkl")
