import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

def menu():
    print("""
=== RH System ===

1 - Adicionar funcionário
2 - Consultar um funcionário 
3 - Atualizar os dados de um funcionário
4 - Excluir um funcionário
5 - Listar todos os funcionários
0 - Sair do sistema
""")

def limpa_tela():
    os.system("cls || clear")


def salvar_funcionario():
    print("Solicitando dados para o usuário: ")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = str(input("Digite seu CPF: "))
    setor = str((input("Digite o seu setor: ")))
    funcao = str(input("Digite sua função: "))
    salario = float(input("Digite o valor do seu salário: "))
    telefone = str(input("Digite o seu telefone: "))
    print("Funcionário adicionado com sucesso")
    funcionario = Funcionario(nome = nome, idade = idade, cpf = cpf, setor = setor, funcao = funcao, salario = salario, telefone = telefone)
    session.add(funcionario)
    session.commit()

def pesquisar_um_funcionario():
    procurar_funcionario = input("Digite o cpf do usuário para ser consultado: ")
    funcionario = session.query(Funcionario).filter_by(cpf = procurar_funcionario).first()
    lista_funcionarios_consulta = session.query(Funcionario).all()
    for funcionario in lista_funcionarios_consulta:
        print(f"Nome: {funcionario.nome}")
        print(f"Idade{funcionario.idade}")
        print(f"CPF: {funcionario.cpf}")
        print(f"Setor: {funcionario.setor}")
        print(f"Função: {funcionario.funcao}")
        print(f"Salário: {funcionario.salario}")
        print(f"Telefone: {funcionario.telefone}")
        

def atualizar_funcionario():
    cpf_funcionario = input("Digite o cpf do usuário para ser atualizado: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
    if funcionario:
        funcionario.nome = input("Digite seu nome: ")
        funcionario.idade = int(input("Digite sua idade: "))
        funcionario.cpf = input("Digite seu cpf: ")
        funcionario.setor = input("Digite seu setor: ")
        funcionario.funcao = input("Digite sua função: ")
        funcionario.salario = float(input("Digite seu salário: "))
        funcionario.telefone = input("Digite seu telefone(com DDD): ")
        session.commit()
        print(f"{funcionario.nome} atualizado com sucesso")
    else:
        print("Erro ao atualizar. Tente Novamente")

def excluir_funcionario():
    cpf_funcinario = input("Digite o cpf do usuário que será excluido: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcinario).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.nome} excluído com sucesso")
    else:
        print("Erro ao excluir")


def listar_todos_funcionarios():
    lista_funcionarios_todos = session.query(Funcionario).all()

    for funcionario in lista_funcionarios_todos:
        print(f"Número: {funcionario.id} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - CPF: {funcionario.cpf} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário{funcionario.salario} - Telefone(com DDD):{funcionario.telefone}")

#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#criando tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key = True, autoincrement= True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", String,)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)
    telefone = Column("telefone", String)

    def __init__(self, nome:str, idade:int, cpf:str, setor:str, funcao:str, salario:float, telefone:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
    

#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

limpa_tela()
while True:
    menu()
    opcao = int(input("Digite a opção que deseja selecionar: "))
    match opcao:
        case 1:
            salvar_funcionario()
        case 2:
            pesquisar_um_funcionario()
        case 3:
            atualizar_funcionario()
        case 4:
            excluir_funcionario()
        case 5:
            listar_todos_funcionarios()
        case 0:
            break
        case _:
            print("Opção inválida. Tente Novamente")








            