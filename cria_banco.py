import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS test (id real PRIMARY KEY, duration real,fhr_valeu real, token text, date_created text, device_id real)"
cria_test = "INSERT INTO test VALUES(1.0, 12.0, 123.0, '00-00-00-00','2020-11-27', 1 )"

cursor.execute(cria_tabela)
cursor.execute(cria_test)

connection.commit()
connection.close()