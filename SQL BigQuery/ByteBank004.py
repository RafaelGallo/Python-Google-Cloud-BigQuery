#pip install --upgrade google-cloud-bigquery

from google.cloud import bigquery

client = bigquery.Client(project="curso-big-query-0965")

table_idAgencias = "curso-big-query-0965.BYTEBANK_PYTHON.AGENCIAS"
table_idClientes = "curso-big-query-0965.BYTEBANK_PYTHON.CLIENTES"
table_idContasCorrente = "curso-big-query-0965.BYTEBANK_PYTHON.CONTAS_CORRENTE"

client.delete_table(table_idAgencias,not_found_ok=True)
client.delete_table(table_idClientes,not_found_ok=True)
client.delete_table(table_idContasCorrente,not_found_ok=True)

print("Tabelas excluidas com sucesso")