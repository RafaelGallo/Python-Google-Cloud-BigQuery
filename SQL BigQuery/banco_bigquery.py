  from google.cloud import bigquery

  client = bigquery.Client(project="datascience2-322514")

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

  table_idAgencias = "datascience2-322514.BYTEBANK_PYTHON.AGENCIAS"
  tableAgencias = bigquery.Table(table_idAgencias, schemaAgencia)
  tableAgencias = client.create_table(tableAgencias)

  table_idClientes = "datascience2-322514.BYTEBANK_PYTHON.CLIENTES"
  tableClientes = bigquery.Table(table_idClientes, schemaCliente)
  tableClientes = client.create_table(tableClientes)

  table_idContasCorrente = "datascience2-322514.BYTEBANK_PYTHON.CONTAS_CORRENTE"
  tableContasCorrente = bigquery.Table(table_idContasCorrente, schemaContaCorrente)
  tableContasCorrente = client.create_table(tableContasCorrente)

  print("Tabelas Criadas")