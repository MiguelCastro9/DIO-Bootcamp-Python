# relational database in python

import sqlite3
import os

try:
    conexao = sqlite3.connect("clients.db")
    print(conexao)

    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), email VARCHAR(150))")

    data_insert = "miguel castro", "miguel@email.com"
    cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data_insert)

    data_update = "miguel castro do nascimento", "miguelcastro@email.com"
    cursor.execute("UPDATE clients SET name=?, email=? WHERE id=1", data_update)

    cursor.execute("SELECT * FROM clients WHERE id=1")
    result_one = cursor.fetchone()
    print(result_one)

    cursor.execute("INSERT INTO clients (name, email) VALUES ('fulano da silva', 'fulano@email.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('ciclano ferreira', 'ciclano@email.com')")
    cursor.execute("INSERT INTO clients (name, email) VALUES ('beutrano de souza', 'beutrano@email.com')")
    cursor.execute("SELECT * FROM clients")
    result_all = cursor.fetchall()
    print(result_all)

    cursor.execute("DELETE FROM clients WHERE id=1")

    conexao.commit()

except Exception as exc:
    conexao.rollback()

os.remove("clients.db")