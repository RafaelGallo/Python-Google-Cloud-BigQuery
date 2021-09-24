from google.cloud import bigquery

# Consulta no bigquey
client = bigquery.Client()
consulaSQL = "SELECT Desc_Vendedor, Cod_Gerente FROM `datascience2-322514.Banco01.dim_organizacional` LIMIT 1000"
consulta = client.query(consulaSQL)

# Resultado no BigQuery
resultado_SQL = consulta.result()

# Resultado da consulta
for x in resultado_SQL:
    print("Cod_Gerente:" + str(x.Cod_Gerente) + ", Desc_Vendedor:" + x.Desc_Vendedor)
