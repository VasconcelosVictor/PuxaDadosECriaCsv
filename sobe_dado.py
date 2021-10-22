import psycopg2

def sobe_dados():

    print("Aguarde!!! Código em execução")
    db_name = '*****'
    db_host = '*****'
    db_user = 'postgres'
    db_password = '******'
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cursor = connect.cursor()

    sql1= f""" select  cadastro.importacao_lote_fnc(dados,dc.id) from cadastro.dado_campo dc 
                join (select id from (select id,max(fim) from 
                (select id, (json_array_elements(dados -> 'unidade') ->> 'fimCadastro')::date as fim from cadastro.dado_campo
                where dthr_proc is null) a group by id)b where max =now()::date)c
                on dc.id = c.id order by (select max((value->>'fimCadastro')::timestamp) from json_array_elements(dados-> 'unidade'))"""

    cursor.execute(sql1)

    sql = """select count(*) from cadastro.unidade where inicio_cadastro::date = now()::date"""
    cursor.execute(sql)
    result = cursor.fetchall()

    qtd_dados = 0

    for dado in result:
        qtd_dados=dado[0]

    connect.commit()
    cursor.close()
    connect.close()

    print("###############################100%")

    return f"Dados Campo Concluído!\nQuantidade de dados: {str(qtd_dados)}"
