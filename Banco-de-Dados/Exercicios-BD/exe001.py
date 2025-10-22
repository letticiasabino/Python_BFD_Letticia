# Crie uma tabela e estabeleça conexão entre elas com as seguintes colunas: ID, nome, idade, cpf, email, endereço, sexo, salario.

import sqlite3 # Primeiro passo é importar o sqlite3

con = sqlite3.connect("cadastro.db") # Aqui estou criando o banco de dados

cursor = con.cursor() # Conectando o banco de dados com a tabela

print("Banco de dados conectado com sucesso!")

# Criando a tabela

cursor.execute("""CREATE TABLE IF NOT EXISTS CadastroCliente (  
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade NUMBER NOT NULL,
               cpf TEXT NOT NULL,
               email TEXT NOT NULL,
               endereço TEXT NOT NULL,
               sexo TEXT NOT NULL,
               salario NUMBER NOT NULL); """)

print("Tabela criada com sucesso!")

# Inserindo as informações 

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Lettícia Sabino", 26, "000.000.000-00", "letticiasabino@email.com", "São Gonaçalo", "F", "25000"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Thamara Araujo", 70, "100.100.100-10", "thamaraaraujo@email.com", "Rio de Janeiro", "F", "3500"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Luis Fernando", 26, "200.200.200-20", "luisfernando@email.com", "Brasília", "M", "2950"))

print("Clientes cadastrados com sucesso.")

# Consultando os dados da tabela

cursor.execute("SELECT * FROM CadastroCliente;") # Selecionando todo o conteúdo da tabela CadastroCliente

resultado = cursor.fetchall() # Criando variável para guardar o resultado da consulta

print("Lista de Clientes")

print("=="*30)
for i in resultado:
    print(f"ID: {i[0]}, Cliente: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, E-mail: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}")

print(resultado)
print("=="*30)
print("\n")

# Consulta filtrada

cursor.execute("SELECT * FROM CadastroCliente WHERE cpf = '000.000.000-00';") # Aqui vai retornar apenas os cpfs que contem essa numeração "000.000.000-00"
cpf = cursor.fetchall()

print("CPF de Lettícia: {cpf}\n")

for e in cpf:
    print(f"ID: {e[0]}, Cliente: {e[1]}, Idade: {e[2]}, CPF: {e[3]}, E-mail: {e[4]}, Endereço: {e[5]}, Sexo: {e[6]}, Salário: {e[7]}")
print(cpf)

con.commit()
con.close()
