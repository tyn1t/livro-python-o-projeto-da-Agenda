import re
import sqlite3 
from contextlib import closing

#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("""create table Agenda(
#                            nome text,
#                            telefone text
#                    )""")
#        cursor.execute("""insert into Agenda( nome,telefone) values(?,?)""",("Nilo","0987-6543"))
#    conexao.commit()

#conexao = sqlite3.connect('Agenda.db')
#cursor = conexao.cursor()
#cursor.execute("select * from Agenda")
#relsutado = cursor.fetchone()
#print(f"Nome:{relsutado[0]} Telefone:{relsutado[1]}")
#cursor.close()
#conexao.close()

#dados =[("joão","2345-6788"),
#       ("André","2345-2345"),
#        ("Maria","9782-2344")]
#conexao = sqlite3.connect("Agenda.db")
#cursor = conexao.cursor()
#cursor.executemany('''
#            insert into Agenda (nome, telefone)
#            values(?,?)
#            ''', dados)
#conexao.commit()
#cursor.close()
#conexao.close()


#conexao = sqlite3.connect("Agenda.db")
#cursor = conexao.cursor()
#cursor.execute("select *from Agenda")
#resultado = cursor.fetchall()
#for registro in resultado: 
#    print(f"Nome:{registro[0]} Telefone{registro[1]}")
#cursor.close()
#conexao.close()


#with sqlite3.connect('Agenda.db') as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("select * from Agenda")
#        while True: 
#            resultado = cursor.fetchone()
#            if resultado is None: 
#                break 
#            print(f"Nome:{resultado[0]} Telefone{resultado[1]}")

#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("select * from Agenda where nome= 'nilo'")
#        while True: 
#            resultada = cursor.fetchone()
#            if resultada is None: 
#                break 
#            print(f"Nome:{resultada[0]} Telefone{resultada[1]}")


#nome = input("Nome a selecionar:")
#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute(f'select * from Agenda where nome= "{nome}"')
#        while True: 
#            resultado = cursor.fetchone()
#            if resultado is None: 
#                break 
#            print(f"Nome:{resultado[0]} Telefone:{resultado[1]}")


#nome = input("Nome a seleleciona: ")
#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute('select * from Agenda where nome = ?', (nome,))
#        x = 0 
#        while True: 
#            resultado = cursor.fetchone()
#            if resultado is None: 
#                if x == 0: 
#                    print("Nada encontrado.")
#                break
#            print(f"Nome: {resultado[0]} Telefone:{resultado[1]}")
#            x += 1

#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("""update Agenda
#                          set telefone = "1234-5678"
#                          where nome = 'nilo'""")
#    conexao.commit()

#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("""update Agenda
#                        set telefone = '1234-5678'""")
#        print('Registro alterados:',cursor.rowcount)
#        if cursor.rowcount == 4: 
#            conexao.commit()
#            print("Alterações gravadas")
#        else: 
#            conexao.rollback()
#            print("Alterações abortadas")


#with sqlite3.connect("Agenda.db") as conexao: 
#    with closing(conexao.cursor()) as cursor: 
#        cursor.execute("""delete from Agenda
#                            where nome = 'Maria'""") 
#        print("registro apagado:", cursor.rowcount)
#        if cursor.rowcount == 1:
#            conexao.commit() 
#            print("Alterações Gravadas")
#        else: 
#            print("Alterações abotadas")
#            conexao.rollback()


#with sqlite3.connect("Agenda.db") as conexao:
#    for resultado in  conexao.execute("select * from Agenda"):
#        print(f"Nome:{resultado[0]},Telefone:{resultado[1]}")


#with sqlite3.connect("Agenda.db") as conexao:
#    conexao.row_factory = sqlite3.Row
#    with closing(conexao.cursor()) as cursor: 
#        for registro in cursor.execute('select * from Agenda'):
#            print(f"Nome:{registro['Nome']} Telefone:{registro['Telefone']}")


