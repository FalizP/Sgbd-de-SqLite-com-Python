import sqlite3
import os
from colorama import Fore as fc, init
init(autoreset=True)


def main():
    clear()
    try:
        conexao, cursor = __enter__()
        with conexao:
            # criarTabela('tb_contatos', cursor)
            # commitDados(conexao, cursor)
            # deleteDados(conexao, cursor)
            # updateDados(conexao, cursor)
            # consultaDados(cursor)
            # deleteTabela("tb_contatos", cursor)
            mostraTabela(cursor)
    except Exception as e:
        print(f'{fc.RED + str(e)}')
    finally:
        __exit__(conexao)
        conexao.close()
        print(f'{fc.LIGHTMAGENTA_EX}------------------------------------------------')
        print(f'{fc.GREEN}Todas as consultas finalizadas!')


def __enter__():
    caminho = r'./sql/agenda.db'
    return conexaoBanco(caminho)


def __exit__(conexao):
    conexao.close()


def conexaoBanco(caminho):
    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor()
    return conexao, cursor


def criarTabela(nomeTabela, cursor):
    sql = f"""
CREATE TABLE {nomeTabela}(
    N_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOME VARCHAR(30),
    T_NICKNAME VARCHAR(15),
    N_TELEFONE INTEGER (14),
    T_EMAIL VARCHAR(30)
);
"""
    cursor.execute(sql)
    print(f'{fc.GREEN}Tabela {fc.YELLOW + nomeTabela + fc.GREEN} criada!')


def commitDados(conexao, cursor):
    nome: str = 'Luiz'
    nickname: str = r'FalizP'
    telefone: int = 123456789
    email: str = r'luizpalma16@gmail.com'
    sql = f"""
INSERT INTO tb_contatos(
    T_NOME,
    T_NICKNAME,
    N_TELEFONE,
    T_EMAIL
)
VALUES( "{nome}", "{nickname}", {telefone}, "{email}")
"""
    cursor.execute(sql)
    conexao.commit()
    print(f'{fc.GREEN}Registro inserido!')


def deleteDados(conexao, cursor):
    tabela = 'tb_contatos'
    coluna = 'T_NOME'
    valor = ''
    sql = f"""
        DELETE FROM {tabela} WHERE {coluna}="{valor}"
"""
    cursor.execute(sql)
    conexao.commit()
    print(f'{fc.GREEN}Registro Removido!')


def updateDados(conexao, cursor):
    tabela = 'tb_contatos'
    nomeColuna = 'T_NICKNAME'
    valorColuna = r'Faliz_007'
    condicao = "N_ID"
    valorCondicao = r'1'
    sql = f"""
        UPDATE {tabela} SET {nomeColuna}="{valorColuna}" WHERE {condicao}="{valorCondicao}"
        """
    cursor.execute(sql)
    conexao.commit()
    print(f'{fc.GREEN}Registro atualizado!')


def consultaDados(cursor):
    campoConsulta = '*'
    tabela = 'tb_contatos'
    nomeColuna = 'T_NOME'
    valorColuna = r'Luiz'
    sql = f"""
    SELECT {campoConsulta} FROM {tabela} WHERE {nomeColuna}="{valorColuna}"
    """
    cursor.execute(sql)
    resultadoConsulta = cursor.fetchall()
    formataConsultaDados(resultadoConsulta)


def mostraTabela(cursor):
    tabela = 'tb_contatos'
    sql = f"""
    SELECT * FROM {tabela}
    """
    cursor.execute(sql)
    resultadoConsulta = cursor.fetchall()
    formataConsultaDados(resultadoConsulta)


def formataConsultaDados(dados):
    for dado in dados:
        print(f'{fc.YELLOW + str(dado)}')
        print(f'{fc.LIGHTBLUE_EX}------------------------------------------------')


def deleteTabela(nomeTabela, cursor):
    sql = f"""
    DROP TABLE IF EXISTS {nomeTabela}
    """
    while True:
        confimacao = str(input(
            f'{fc.YELLOW}Você realmente deseja REMOVER a tabela: {fc.LIGHTRED_EX + nomeTabela + fc.YELLOW}?  [s/n] '))
        if confimacao == 's':
            cursor.execute(sql)
            print(
                f'{fc.GREEN}Tabela {fc.LIGHTRED_EX + nomeTabela + fc.GREEN} removida!')
            return
        elif confimacao == 'n':
            print(
                f'{fc.YELLOW}Tabela {fc.LIGHTRED_EX + nomeTabela + fc.YELLOW} NÃO removida!')
            return


def clear():
    os.system('cls')


if __name__ == '__main__':
    main()
