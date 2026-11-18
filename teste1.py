import sqlite3 #é um comando do Python utilizado para importar o módulo SQLite3

try: #serve para tentar executar um código que pode gerar um erro, evitando que o programa seja interrompido
    banco = sqlite3.connect('banco.db')
    #permite que seu programa Python tenha acesso a um banco de dados para armazenar informações permanente
    cursor = banco.cursor()
    #serve para criar um cursor que permite executar comandos SQL no banco de dados SQLite

    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")
    #serve para criar uma tabela chamada aluno dentro do banco de dados SQLite
    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")
    #serve para cadastrar um novo aluno na tabela aluno do banco de dados SQLite
    banco.commit() #serve para confirmar e salvar as alterações no banco de dados
    print("Os dados foram adicionados com sucesso!!") #Serve para informar s confirmação do cadastro


    cursor.execute("Select *FROM aluno") #Serve para consutar os alunos cadastrados, colunas e registro da tabela
    print(cursor.fetchall()) 
    #serve para recuperar e exibir todos os registros encontrados na consulta do banco de dados
    cursor.execute("DELETE from aluno WHERE idade = 20")
    #Serve para excluir a tabela aluno que possui idade acima de 20

    banco.commit() #Serva para confirmar e salvar as alterações no banco de dados
    banco.close() #serve para fechar a conexão com o banco de dados depois que o programa termina de realizar suas operações
    print("Os dados foram removidos com sucesso!!")
    #serve para exibir uma mensagem na tela informando que os dados foram removidos do banco de dados
except sqlite3.Error as erro:
    #serve para identificar erros do banco de dados e permitir que o programa informe o problema sem simplesmente encerrar inesperadamente
    print("Erro ao excluir: ", erro)
    #serve para mostrar uma mensagem de erro na tela caso aconteça algum problema durante a exclusão de dados do banco de dados