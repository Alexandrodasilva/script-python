import psycopg2 
from datetime import datetime

db_params = {
    "host": "",
    "database" : "",
    "user": "",
    "password": ""
}

try:
    conn = psycopg2.connect(**db_params)
    print("Conexão bem-sucedida ao banco de dados.")
    cursor = conn.cursor()

except psycopg2.Error as error:
     print("Erro durante a conexão com o banco de dados:", error)

nome_arquivo_entrada = "datas.txt"
nome_arquivo_saida = "saida.txt"

with open(nome_arquivo_entrada, "r") as arquivo:
    with open(nome_arquivo_saida, "w") as arquivo_saida:
        for linha in arquivo:
            valores = linha.split()
            if(len(valores) > 1):

                    data_original = valores[0]
                    data_objeto = datetime.strptime(data_original, "%d-%m-%Y")
                    data_formatada = data_objeto.strftime("%Y-%m-%d")

                    data_original1 = valores[1]
                    data_objeto1 = datetime.strptime(data_original1, "%d-%m-%Y")
                    data_formatada1 = data_objeto1.strftime("%Y-%m-%d")

                    start_date = data_formatada + " 00:00:00"
                    end_date = data_formatada1 + " 23:59:59"
                    sql_query = """
                    SELECT COUNT(id)
                    FROM tabela
                    WHERE data_hora_entrada BETWEEN %s AND %s;
                    """
                    cursor.execute(sql_query, (start_date, end_date))
                    result = cursor.fetchone()[0]
                    arquivo_saida.write(str(data_formatada) + " a " + str(data_formatada1) +", Quantidade: " + str(result) + "\n")
                    # print(f"resultados: {result}")
cursor.close()
conn.close()
