# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144Y74ZkzBSPRBLLmozbVXOEF-LxtEkux
"""

from sqlalchemy import create_engine
from sqlalchemy import text
my_conn = create_engine("sqlite:////content/my_db.db")

conn = my_conn.connect()

# Importer les modules nécessaires
from sqlalchemy import create_engine, text
import pandas as pd

# Créer un engine pour une base de données SQLite située dans "/content/my_db.db"
engine = create_engine("sqlite:////content/my_db.db")

# Établir une connexion à la base de données
conn = engine.connect()

# Exécuter la requête et récupérer les résultats
result_set = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))

# Afficher les noms des tables
for row in result_set:
    print(row[0])

#print(engine.sqlite_master())

# Établir une connexion à la base de données
conn = engine.connect()

# TO DO: Écrire une requête pour extraire toutes les données de la table "student"
query = text("SELECT * FROM student")

# Exécuter la requête et récupérer les résultats
result_set = conn.execute(query)

# TO DO: Afficher les données récupérées sous forme de dataframe pandas
df = pd.DataFrame(result_set.fetchall(),columns=result_set.keys())
df
