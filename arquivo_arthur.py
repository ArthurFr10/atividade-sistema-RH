import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

def menu():
    print("""
=== RH System ===

1 - Adicionar funcionário
2 - Consultar um funcionário 
3 - Atualizar os dados de um funcionário
4 - Excluir um uncionário
5 - Listar todos os funcionários
6 - Sair do sistema
""")

def limpa_tela():
    os.system("cls || clear")

limpa_tela()

def pesquisar_um_funcionario():
    lista_funcionarios = session.query(Funcionario).all()

    for funcionario in lista_funcionarios:
        print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")

def atualizar_funcionario():
    cpf_funcionario = input("Informe o cpf do usuário para ele ser atualizado: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
    dados_novos = Funcionario(
        nome = input("Digite seu nome: "),
        idade = input("Digite sua idade: "),
        cpf = input("Digite seu cpf: "),
        setor = input("Digite seu setor: "),
        funcao = input("Digite sua função: "),
        salario = input("Digite seu salário: "),
        telefone = input("Digite seu telefone: "),
    )
    funcionario = dados_novos
    session.add(funcionario)
    session.commit()

def excluir_funcionario():
    cpf_funcinario = input("Digite o cpf do usuário que será excluido: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcinario).first()
    session.delete(funcionario)
    session.commit()
    print(f"{funcionario.nome} excluído com sucesso")
#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#criando tabela
Base = declarative_base()

class Funcionario():
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key = True, autoincrement= True )
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)

    def __init__(self, nome:str, idade:int, cpf:float, setor:str, funcao:str, salario:float, telefone:float):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
    
def salvar_funcionario(nomes, idades, cpfs, setores, funcoes, salarios, telefones):
    funcionario = Funcionario(nome =nomes, idade = idades, cpf = cpfs, setor = setores, funcao = funcoes, salario = salarios, telefone = telefones)
    session.add(funcionario)
    session.commit()

#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

while True:
    menu()
    opcao = int(input("Digite a opção que deseja selecionar: "))
    match opcao:
        case 1: 

            print("Solicitando dados para o usuário: ")
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cpf = float(input("Digite seu CPF: "))
            setor = str((input("Digite o seu setor: ")))
            funcao = str(input("Digite sua função: "))
            salario = float(input("Digite o valor do seu salário: "))
            telefone = float(input("Digite o seu telefone: "))
            salvar_funcionario(nome, idade, cpf, setor, funcao, salario, telefone)

        case 2:
            pesquisar_um_funcionario()
        
        case 3:
        
        case 4:
            excluir_funcionario()            






            