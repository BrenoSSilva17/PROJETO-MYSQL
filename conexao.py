import mysql.connector 
from dotenv import load_dotenv
import os
# pip install dotenv 
# pip install mysql-connector-python 

#Carregar asv variaveis de ambiente (.env)
load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="faculdade",
            port=3307
        )
        cursor = conexao.cursor()
        print("Conexão estabelicida")
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão: {erro}")
        return None, None

