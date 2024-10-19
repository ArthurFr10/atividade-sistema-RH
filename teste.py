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
6 - Sair do sistema
""")

def limpa_tela():
    os.system("cls || clear")

limpa_tela()

def salvar_funcionario():
    print("Solicitando dados para o usuário: ")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")
    setor = input("Digite o seu setor: ")
    funcao = input("Digite sua função: ")
    salario = float(input("Digite o valor do seu salário: "))
    telefone = input("Digite o seu telefone: ")
    
    novo_funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
    session.add(novo_funcionario)
    session.commit()

def atualizar_funcionario():
    cpf_funcionario = input("Informe o CPF do usuário para ele ser atualizado: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf_funcionario).first()
    
    if funcionario:
        funcionario.nome = input("Digite seu nome: ")
        funcionario.idade = int(input("Digite sua idade: "))
        funcionario.cpf = input("Digite seu CPF: ")
        funcionario.setor = input("Digite seu setor: ")
        funcionario.funcao = input("Digite sua função: ")
        funcionario.salario = float(input("Digite seu salário: "))
        funcionario.telefone = input("Digite seu telefone: ")
        
        session.commit()
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario():
    cpf_funcionario = input("Digite o CPF do usuário que será excluído: ")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf_funcionario).first()
    
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.nome} excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

def listar_todos_funcionarios():
    lista_funcionarios = session.query(Funcionario).all()

    for funcionario in lista_funcionarios:
        print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", String)
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

# Criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

while True:
    menu()
    opcao = int(input("Digite a opção que deseja selecionar: "))
    match opcao:
        case 1:
            salvar_funcionario()
        case 3:
            atualizar_funcionario()
        case 4:
            excluir_funcionario()
        case 5:
            listar_todos_funcionarios()
        case 6:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida. Tente novamente.")