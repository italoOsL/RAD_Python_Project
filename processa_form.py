import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='seu_usuario',
            password='sua_senha',
            database='registro_notas'  
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return None

def executar_sql(comando, parametros=None):
    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        if parametros:
            cursor.execute(comando, parametros)
        else:
            cursor.execute(comando)
        conexao.commit()
        return cursor
    except mysql.connector.Error as err:
        print("Erro ao executar o comando SQL:", err)
    finally:
        cursor.close()
        conexao.close()

def criar_tabela():
    sql1 = '''CREATE TABLE IF NOT EXISTS tbaluno (
        matricula INT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        curso VARCHAR(100) NOT NULL,
        PRIMARY KEY (matricula)
        );'''
    sql2 = '''CREATE TABLE IF NOT EXISTS tbnota (
        item INT PRIMARY KEY AUTO_INCREMENT,
        valor FLOAT NOT NULL,
        matricula INT NOT NULL,
        FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
        );'''
    executar_sql(sql1)
    executar_sql(sql2)
    print('Banco de dados ok')

def inserir_dados_alunos():
    m = int(input('Digite a matrícula:'))
    n = input('Digite o nome:')
    c = input('Digite o curso:')
    nota = float(input('Digite a nota:'))
    
    sql1 = '''INSERT INTO tbaluno (matricula, nome, curso)
              VALUES (%s, %s, %s);'''
    sql2 = '''INSERT INTO tbnota (valor, matricula)
              VALUES (%s, %s);'''
    
    executar_sql(sql1, (m, n, c))
    executar_sql(sql2, (nota, m))
    print('Dados inseridos!!!')

def alterar_dados():
    m = int(input('Digite a matrícula do aluno:'))
    n = input('Digite o nome completo:')
    c = input('Digite o novo curso:')
    
    comando = 'UPDATE tbaluno SET nome=%s, curso=%s WHERE matricula=%s;'
    executar_sql(comando, (n, c, m))
    print('Dados alterados!!!')

def excluir_dados():
    m = int(input('Digite a matrícula do aluno a excluir:'))
    
    comando1 = 'DELETE FROM tbnota WHERE matricula=%s;'
    comando2 = 'DELETE FROM tbaluno WHERE matricula=%s;'
    
    executar_sql(comando1, (m,))
    executar_sql(comando2, (m,))
    print('Registro excluído!!!')

def consultar_aluno():
    m = int(input('Digite a matrícula do aluno a consultar:'))
    
    comando = 'SELECT nome, curso FROM tbaluno WHERE matricula=%s;'
    cursor = executar_sql(comando, (m,))
    
    if cursor:
        resultado = cursor.fetchone()
        if resultado:
            print(f'Matrícula: {m}, Nome: {resultado[0]}, Curso: {resultado[1]}')
        else:
            print('Aluno não encontrado.')

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Inserir Aluno")
        print("2. Consultar Aluno")
        print("3. Alterar Dados do Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            inserir_dados_alunos()
        elif opcao == '2':
            consultar_aluno()
        elif opcao == '3':
            alterar_dados()
        elif opcao == '4':
            excluir_dados()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar funções
criar_tabela()
menu()  # Chama o menu interativo
print("Fim do programa")