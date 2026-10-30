import sqlite3

def conexao_banco():
    conexao = sqlite3.connect("contatos.db")

    cursor = conexao.cursor()

    sql ='''CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    );'''
    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        INSERT INTO contatos (nome, telefone, email) 
        VALUES (?, ?, ?)'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()
    

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        SELECT * FROM contatos'''
    cursor.execute(sql)
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos) > 0:
        print('-' * 67)
        print("### LISTA DE CONTATOS ###".center(67))
        print('-' * 67)
        print(f"{'ID':<5} | {'Nome':<15} | {'Telefone':<15} | {'Email':<30}")
        print('-' * 67)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<15} | {contato[2]:<15} | {contato[3]:<30}")
            print('-' * 67)
    else:
        print("Nenhum contato encontrado.")

def buscar_contato_pelo_nome():
    nome = input("Digite o nome do contato que deseja buscar\n")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        SELECT * FROM contatos WHERE nome LIKE ?'''
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos) > 0:
        print('-' * 67)
        print("### RESULTADO DA BUSCA ###".center(67))
        print('-' * 67)
        print(f"{'ID':<5} | {'Nome':<15} | {'Telefone':<15} | {'Email':<30}")
        print('-' * 67)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<15} | {contato[2]:<15} | {contato[3]:<30}")
            print('-' * 67)
    else:
        print("Nenhum contato encontrado com esse nome.")

def atualizar_contato():
    listar_contatos()
    
    id = int(input("Digite o ID do contato que deseja atualizar: "))
    nome = input("Novo nome\n")
    telefone = input("Novo telefone\n")
    email = input("Novo email\n")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        UPDATE contatos SET nome=?, telefone=?, email=? WHERE id=?'''
    cursor.execute(sql, (nome, telefone, email, id))
    conexao.commit()
    conexao.close()
    print("Contato atualizado com sucesso!")


def excluir_contato():
    listar_contatos()
    
    id = int(input("Digite o ID do contato que deseja excluir: "))
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
        DELETE FROM contatos WHERE id=?'''
    cursor.execute(sql, (id,))
    conexao.commit()
    conexao.close()
    print("Contato excluído com sucesso!")

def menu():
    while True:
        print("### CONTATOS ###")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato pelo nome")
        print ("4. Atualizar contato")
        print("5. Excluir contato")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome\n")
            telefone = input("Telefone\n")
            email = input("Email\n")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato_pelo_nome()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "0":
            print("Saindo do sistema. . .")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()