import psycopg2

def gera_planilhas(setor):

    db_name = '*****'
    db_host = '*****'
    db_user = 'postgres'
    db_password = '*****'
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cursor = connect.cursor()

    sql1= f"""select quadra,numero_porta,c.complemento,nome_proprietario,cpf,setor, c.lote_id from stage.consulta c
        where setor = {setor}
        and area_trabalho = 3
        order by quadra"""

    cursor.execute(sql1)
    result1 = cursor.fetchall()


    for dado in result1:
        with open( f'C:/Users/topo/Desktop/setor_Setor/setor_{setor}_area_3.csv', 'a+') as arquivo:
            print(str(dado[0])+','+str(dado[1])+','+str(dado[2])+','+str(dado[3])+','+str(dado[4])+','+str(dado[5])+','+str(dado[6]), file=arquivo)

    connect.commit()
    cursor.close()
    connect.close()

    return('Concluído!')