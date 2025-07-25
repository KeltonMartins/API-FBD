import psycopg2

#conexão com o banco de dados
def get_connection():
    #retorna a conexão com o banco de dados local
    return psycopg2.connect(
        dbname = "DTB_Volley",
        user = "postgres",
        password = "12345",
        host = "localhost"
    )