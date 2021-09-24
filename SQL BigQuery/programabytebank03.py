import bigquery

client = bigquery.Client(project="curso-big-query-0965")

schemaAgencia = [
    bigquery.SchemaField("NUMERO_AGENCIA","STRING"),
    bigquery.SchemaField("NOME_AGENCIA","STRING")
    ]
schemaCliente = [
    bigquery.SchemaField("CPF","STRING"),
    bigquery.SchemaField("NOME_CLIENTE","STRING")
    ]
schemaContaCorrente = [
    bigquery.SchemaField("NUMERO_CONTA","STRING"),
    bigquery.SchemaField("NUMERO_AGENCIA","STRING"), 
    bigquery.SchemaField("NOME_CLIENTE","STRING"),
    bigquery.SchemaField("TIPO_CONTA","INTEGER")
    ]

table_idAgencias = "curso-big-query-0965.BYTEBANK_PYTHON.AGENCIAS"
uriAgencias = "gs://curso-big-query-0965/Exercicios/Agencias.csv"
job_configAgencias = bigquery.LoadJobConfig(schema=schemaAgencia, skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)
load_jobAgencias = client.load_table_from_uri(source_uris=uriAgencias, destination=table_idAgencias, job_config=job_configAgencias)
load_jobAgencias.result()

table_idClientes = "curso-big-query-0965.BYTEBANK_PYTHON.CLIENTES"
uriClientes = "gs://curso-big-query-0965/Exercicios/Clientes.csv"
job_configClientes = bigquery.LoadJobConfig(schema=schemaCliente, skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)
load_jobClientes = client.load_table_from_uri(source_uris=uriClientes, destination=table_idClientes, job_config=job_configClientes)
load_jobClientes.result()

table_idContasCorrente = "curso-big-query-0965.BYTEBANK_PYTHON.CONTAS_CORRENTE"
uriContasCorrente = "gs://curso-big-query-0965/Exercicios/ContasCorrente.csv"
job_configContasCorrente = bigquery.LoadJobConfig(schema=schemaContaCorrente, skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)
load_jobContasCorrente = client.load_table_from_uri(source_uris=uriContasCorrente, destination=table_idContasCorrente, job_config=job_configContasCorrente)
load_jobContasCorrente.result()

print("TABELAS CARREGADAS")